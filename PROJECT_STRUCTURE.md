# Data Drift & Quality Management System

A full-stack web application for monitoring data quality and detecting data drift in CSV datasets using statistical methods and pandas for data preprocessing.

## Project Structure

```
/app/
├── backend/                        # FastAPI Backend
│   ├── server.py                  # Main API server with endpoints
│   ├── spark_processor.py         # Data processing using pandas
│   ├── quality_checker.py         # Data quality analysis module
│   ├── drift_detector.py          # Drift detection algorithms
│   ├── requirements.txt           # Python dependencies
│   └── .env                       # Environment variables
│
├── frontend/                      # React Frontend
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.js       # Main dashboard with upload
│   │   │   ├── QualityAnalysis.js # Data quality analysis page
│   │   │   ├── DriftDetection.js  # Drift detection comparison
│   │   │   └── Reports.js         # Historical reports view
│   │   ├── components/
│   │   │   ├── Layout.js          # App layout with sidebar
│   │   │   └── ui/                # Shadcn UI components
│   │   ├── App.js                 # Main app with routing
│   │   ├── App.css                # Global styles
│   │   └── index.css              # Tailwind styles
│   ├── package.json
│   ├── craco.config.js            # CRACO configuration
│   └── .env                       # Frontend environment variables
│
└── PROJECT_STRUCTURE.md           # This file
```

## Key Features

### 1. Data Quality Analysis
- **Missing Values Detection**: Identifies and quantifies missing data per column
- **Duplicate Detection**: Finds duplicate rows in datasets
- **Outlier Detection**: Uses IQR method to detect statistical outliers
- **Data Type Validation**: Checks and reports data types for all columns
- **Statistical Summary**: Provides comprehensive statistics for numeric and categorical columns

### 2. Data Drift Detection
- **KS Test**: Kolmogorov-Smirnov test for numerical columns
- **Chi-Square Test**: Statistical test for categorical columns
- **PSI Score**: Population Stability Index calculation
- **Column-wise Analysis**: Detailed drift metrics for each column
- **Overall Drift Score**: Aggregated drift metric across all columns

### 3. MongoDB Storage
- Datasets are stored with metadata and raw CSV data
- Quality reports are persisted for historical analysis
- Drift reports are saved for trend monitoring

## Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Pandas**: Data processing and analysis (replaces PySpark for containerized environment)
- **SciPy**: Statistical tests for drift detection
- **scikit-learn**: Machine learning utilities
- **Motor**: Async MongoDB driver
- **Pydantic**: Data validation and serialization

### Frontend
- **React 19**: Latest React with modern features
- **React Router**: Client-side routing
- **Axios**: HTTP client for API calls
- **Shadcn/UI**: Modern UI component library
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Icon library

## API Endpoints

### Dataset Management
- `POST /api/upload` - Upload CSV file
- `GET /api/datasets` - List all datasets

### Quality Analysis
- `POST /api/quality-check/{dataset_id}` - Run quality analysis
- `GET /api/quality-reports/{dataset_id}` - Get quality reports

### Drift Detection
- `POST /api/drift-check?reference_id={ref}&target_id={target}` - Compare datasets
- `GET /api/drift-reports` - Get all drift reports

## How to Run in VSCode

### Prerequisites
- Python 3.11+
- Node.js 18+
- MongoDB (already running in this environment)
- yarn package manager

### Backend Setup
```bash
# Navigate to backend directory
cd /app/backend

# Install dependencies (already done)
pip install -r requirements.txt

# Run server
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd /app/frontend

# Install dependencies (already done)
yarn install

# Run development server
yarn start
```

### Access the Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8001
- API Documentation: http://localhost:8001/docs

## Usage Workflow

1. **Upload Dataset**: 
   - Navigate to Dashboard
   - Upload CSV file via drag-drop or file picker
   - System processes and stores dataset with metadata

2. **Quality Analysis**:
   - Go to Quality Analysis page
   - Select a dataset from dropdown
   - Click "Run Quality Check"
   - View detailed quality metrics:
     - Missing values per column
     - Duplicate rows count
     - Outlier detection results
     - Statistical summaries

3. **Drift Detection**:
   - Navigate to Drift Detection page
   - Select reference dataset (baseline)
   - Select target dataset (current data)
   - Click "Run Drift Detection"
   - View drift analysis:
     - Overall drift status
     - Column-wise drift scores
     - Statistical test results (KS test, Chi-square)
     - PSI scores

4. **Reports**:
   - View historical drift reports
   - Track data quality trends over time

## Data Processing Architecture

### Pandas-Based Processing
Originally designed for PySpark, the system now uses pandas for data processing due to containerized environment constraints. This provides:
- Efficient CSV parsing and data manipulation
- Statistical analysis capabilities
- Easy integration with scipy for advanced statistics
- Lower overhead for moderate dataset sizes

### Statistical Methods

**For Numerical Columns:**
- Kolmogorov-Smirnov (KS) test for distribution comparison
- Population Stability Index (PSI) for drift measurement
- IQR method for outlier detection

**For Categorical Columns:**
- Chi-square test for distribution changes
- Value frequency analysis

## Environment Variables

### Backend (.env)
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=test_database
CORS_ORIGINS=*
```

### Frontend (.env)
```
REACT_APP_BACKEND_URL=https://drift-detector.preview.emergentagent.com
```

## Database Schema

### Datasets Collection
```json
{
  "id": "uuid",
  "filename": "string",
  "upload_date": "datetime",
  "rows": "integer",
  "columns": "integer",
  "column_names": ["array"],
  "file_size": "integer",
  "data_summary": "object",
  "csv_data": "string"
}
```

### Quality Reports Collection
```json
{
  "id": "uuid",
  "dataset_id": "string",
  "report_date": "datetime",
  "missing_values": "object",
  "duplicates": "object",
  "outliers": "object",
  "data_types": "object",
  "statistics": "object"
}
```

### Drift Reports Collection
```json
{
  "id": "uuid",
  "reference_dataset_id": "string",
  "target_dataset_id": "string",
  "report_date": "datetime",
  "drift_detected": "boolean",
  "column_drift": "object",
  "overall_drift_score": "float",
  "test_results": "object"
}
```

## Design Features

- **Modern Dark Sidebar**: Professional navigation with icon-based menu
- **Ocean Blue Theme**: Clean data analytics aesthetic
- **Responsive Cards**: Hover effects and smooth transitions
- **Statistical Visualizations**: Color-coded metrics for quick insights
- **Gradient Accents**: Subtle use for status indicators
- **Space Grotesk + Inter**: Modern font pairing for headings and body text

## Future Enhancements

- Add visualization charts for trends
- Implement scheduled drift monitoring
- Support for more file formats (Excel, Parquet)
- Advanced filtering and search
- Export reports to PDF/Excel
- Real-time drift alerts
- Integration with data pipelines
