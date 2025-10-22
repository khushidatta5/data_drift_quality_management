# Local Setup Guide - Data Drift & Quality Management System

## Getting the Code to Your Desktop

### Step 1: Download the Project
You have two options:

**Option A: Download from Emergent (if available)**
- Use the Emergent platform's download/export feature to get the project files

**Option B: Copy Files Manually**
- Copy all files from `/app/backend/` and `/app/frontend/` directories
- Maintain the same folder structure

## Prerequisites for Local Development

### Required Software:
1. **Python 3.11+** - [Download](https://www.python.org/downloads/)
2. **Node.js 18+** - [Download](https://nodejs.org/)
3. **MongoDB** - [Download](https://www.mongodb.com/try/download/community)
4. **VS Code** - [Download](https://code.visualstudio.com/)
5. **Git** (optional) - [Download](https://git-scm.com/)

### Install Package Managers:
```bash
# Verify Python and pip
python --version
pip --version

# Install yarn (globally)
npm install -g yarn

# Verify installations
yarn --version
node --version
```

## Project Structure on Your Desktop

```
data-drift-project/
├── backend/
│   ├── server.py
│   ├── spark_processor.py
│   ├── quality_checker.py
│   ├── drift_detector.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── craco.config.js
│   └── .env
├── PROJECT_STRUCTURE.md
└── LOCAL_SETUP_GUIDE.md (this file)
```

## Setup Instructions

### Step 1: Install MongoDB Locally

**Windows:**
1. Download MongoDB Community Server
2. Install with default settings
3. MongoDB will run on `mongodb://localhost:27017`

**Mac (using Homebrew):**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

### Step 2: Setup Backend

```bash
# Open VS Code and navigate to project
cd data-drift-project

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Navigate to backend
cd backend

# Install dependencies
pip install -r requirements.txt
```

**Create/Update backend/.env file:**
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=data_drift_db
CORS_ORIGINS=http://localhost:3000
```

**Test Backend:**
```bash
# Run the server
uvicorn server:app --reload --host 0.0.0.0 --port 8001

# You should see:
# INFO:     Uvicorn running on http://0.0.0.0:8001
# INFO:     Application startup complete.
```

Open browser: http://localhost:8001/docs (FastAPI Swagger UI)

### Step 3: Setup Frontend

Open a **new terminal** in VS Code:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
yarn install

# This will take a few minutes
```

**Create/Update frontend/.env file:**
```env
REACT_APP_BACKEND_URL=http://localhost:8001
WDS_SOCKET_PORT=3000
REACT_APP_ENABLE_VISUAL_EDITS=false
ENABLE_HEALTH_CHECK=false
```

**Test Frontend:**
```bash
# Run development server
yarn start

# Browser should auto-open to http://localhost:3000
```

## Running the Application

### Terminal 1 - Backend:
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

### Terminal 2 - Frontend:
```bash
cd frontend
yarn start
```

### Access Points:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8001
- **API Docs**: http://localhost:8001/docs

## VS Code Setup

### Recommended Extensions:
1. **Python** (Microsoft)
2. **Pylance** (Microsoft)
3. **ESLint** (Microsoft)
4. **Prettier** (Prettier)
5. **ES7+ React/Redux/React-Native snippets**
6. **MongoDB for VS Code**
7. **Thunder Client** (API testing)

### VS Code Settings (Optional):

Create `.vscode/settings.json` in project root:
```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

### VS Code Tasks (Optional)

Create `.vscode/tasks.json`:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Backend",
      "type": "shell",
      "command": "cd backend && source venv/bin/activate && uvicorn server:app --reload",
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": false
      }
    },
    {
      "label": "Run Frontend",
      "type": "shell",
      "command": "cd frontend && yarn start",
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": false
      }
    }
  ]
}
```

## Testing the Application

### 1. Upload a CSV File
- Go to Dashboard (http://localhost:3000)
- Drag and drop your CSV file or click to browse
- Should see success message

### 2. Run Quality Check
- Navigate to "Quality Analysis"
- Select your uploaded dataset
- Click "Run Quality Check"
- View detailed quality metrics

### 3. Test Drift Detection
- Upload a second CSV (or modified version)
- Go to "Drift Detection"
- Select reference dataset (baseline)
- Select target dataset (new data)
- Click "Run Drift Detection"
- View drift analysis results

## Troubleshooting

### MongoDB Connection Issues:
```bash
# Check if MongoDB is running
# Windows:
net start MongoDB

# Mac:
brew services list | grep mongodb

# Linux:
sudo systemctl status mongodb
```

### Backend Port Already in Use:
```bash
# Change port in backend startup:
uvicorn server:app --reload --host 0.0.0.0 --port 8002

# Update frontend/.env:
REACT_APP_BACKEND_URL=http://localhost:8002
```

### Frontend Build Issues:
```bash
# Clear cache and reinstall
cd frontend
rm -rf node_modules
rm yarn.lock
yarn install
```

### Python Package Issues:
```bash
# Update pip
pip install --upgrade pip

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

## Development Workflow

### Making Changes:

**Backend Changes:**
- Edit files in `backend/`
- FastAPI auto-reloads (uvicorn --reload)
- No restart needed

**Frontend Changes:**
- Edit files in `frontend/src/`
- React auto-reloads
- Changes appear immediately

### Adding New Dependencies:

**Python:**
```bash
cd backend
pip install <package-name>
pip freeze > requirements.txt
```

**JavaScript:**
```bash
cd frontend
yarn add <package-name>
```

## Production Deployment (Optional)

### Backend:
```bash
# Build for production
pip install gunicorn
gunicorn server:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001
```

### Frontend:
```bash
# Build for production
cd frontend
yarn build

# Serve with static server
npm install -g serve
serve -s build -l 3000
```

## File Editing Tips

### Key Files to Modify:

**Add New API Endpoint:**
- Edit: `backend/server.py`
- Add route with `@api_router.post()` or `@api_router.get()`

**Add New Page:**
1. Create: `frontend/src/pages/NewPage.js`
2. Add route in: `frontend/src/App.js`
3. Add nav item in: `frontend/src/components/Layout.js`

**Modify Data Processing:**
- Edit: `backend/quality_checker.py` or `backend/drift_detector.py`

**Change Styling:**
- Global styles: `frontend/src/App.css`
- Tailwind config: `frontend/tailwind.config.js`
- Component styles: inline in component files

## Support

For issues or questions:
1. Check `PROJECT_STRUCTURE.md` for architecture details
2. Review API docs at http://localhost:8001/docs
3. Check browser console for frontend errors
4. Check terminal logs for backend errors

## Next Steps

Once running locally:
1. Test all features with your own CSV files
2. Customize the UI theme/colors
3. Add new quality checks or drift metrics
4. Integrate with your data pipelines
5. Deploy to cloud (AWS, Azure, GCP)

---

**Note:** This project uses pandas for data processing instead of PySpark to ensure compatibility with standard Python environments without requiring Java/Spark installations.
