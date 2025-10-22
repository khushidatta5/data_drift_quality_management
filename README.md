# 📊 Data Drift & Quality Management System

A full-stack web application for monitoring data quality and detecting data drift in CSV datasets using statistical methods.

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![React](https://img.shields.io/badge/React-19-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-4.5-green)

## 🌟 Features

### Data Quality Analysis
- ✅ Missing values detection with percentage per column
- ✅ Duplicate row identification
- ✅ Outlier detection using IQR method
- ✅ Comprehensive data type validation
- ✅ Statistical summaries for numeric and categorical data

### Data Drift Detection
- 📈 KS Test for numerical columns
- 📊 Chi-Square test for categorical columns
- 🎯 PSI (Population Stability Index) calculation
- 📉 Column-wise drift analysis with p-values
- 🔍 Overall drift score and status

### Modern UI
- 🎨 Clean, professional interface with dark sidebar
- 📱 Responsive design
- 🖱️ Drag-and-drop file upload
- 📋 Interactive data tables
- 📊 Visual metrics and status indicators

## 🚀 Quick Start - Running in VS Code on Your Desktop

### Prerequisites
- Python 3.11+
- Node.js 18+
- MongoDB
- yarn package manager

### Installation Steps

1. **Download/Copy this entire project folder to your desktop**

2. **Open in VS Code**
```bash
code /path/to/data-drift-project
```

3. **Setup Backend** (Terminal 1 in VS Code)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. **Setup Frontend** (Terminal 2 in VS Code)
```bash
cd frontend
yarn install
```

5. **Configure Environment Files**

Create `backend/.env`:
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=data_drift_db
CORS_ORIGINS=http://localhost:3000
```

Create `frontend/.env`:
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

6. **Start MongoDB** (if not running)
```bash
# Mac: brew services start mongodb-community
# Linux: sudo systemctl start mongodb
# Windows: net start MongoDB
```

7. **Run the Application**

Terminal 1 (Backend):
```bash
cd backend
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

Terminal 2 (Frontend):
```bash
cd frontend
yarn start
```

8. **Access the App**
- Frontend: http://localhost:3000
- API Docs: http://localhost:8001/docs

## 📖 Documentation

- **[Local Setup Guide](LOCAL_SETUP_GUIDE.md)** - Detailed VS Code setup instructions
- **[Project Structure](PROJECT_STRUCTURE.md)** - Architecture and file organization

## 🎯 How to Use

1. **Upload CSV**: Drag-drop or click to upload your dataset
2. **Quality Check**: Analyze missing values, duplicates, outliers
3. **Drift Detection**: Compare two datasets to detect distribution changes
4. **View Reports**: Monitor historical drift trends

## 🛠️ Tech Stack

**Backend:** FastAPI, Pandas, SciPy, MongoDB  
**Frontend:** React 19, Shadcn/UI, Tailwind CSS  
**Processing:** Pandas (replaces PySpark for desktop compatibility)

## 📊 File Structure

```
project/
├── backend/              # FastAPI backend
│   ├── server.py        # Main API
│   ├── quality_checker.py
│   ├── drift_detector.py
│   └── requirements.txt
│
├── frontend/            # React frontend
│   ├── src/pages/      # Dashboard, Quality, Drift, Reports
│   └── package.json
│
└── docs/               # Documentation
```

## 🔧 Development in VS Code

- Use split terminals for backend and frontend
- Backend auto-reloads on file changes
- Frontend hot-reloads automatically
- Install recommended VS Code extensions (see LOCAL_SETUP_GUIDE.md)

## 📝 Notes

- Uses pandas instead of PySpark for desktop compatibility
- No Java/Spark installation required
- MongoDB stores datasets and reports
- All processing done locally on your machine

For complete setup instructions and troubleshooting, see **[LOCAL_SETUP_GUIDE.md](LOCAL_SETUP_GUIDE.md)**
