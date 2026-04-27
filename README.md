# African Climate Trend Analysis - Week 0

This project focuses on analyzing historical climate data from Ethiopia, Kenya, Sudan, Tanzania, and Nigeria (2015–2026) to support Ethiopia's position for COP32.

## Project Structure
- `.github/workflows/`: Contains CI/CD pipelines (GitHub Actions) for automated testing and environment validation.
- `notebooks/`: Country-specific Jupyter notebooks for Exploratory Data Analysis and visualization.
- `scripts/`: Modular Python scripts for data cleaning, outlier detection, and statistical processing.
- `src/`: Core utility functions and reusable source code.
- `tests/`: Unit tests to ensure the integrity of the data processing pipeline.
- `data/`: (Local only) Target directory for raw and cleaned datasets. **Note: This folder is git-ignored.**

---
## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/hk12214/climate-challenge-week0.git
cd climate-challenge-week0 
```
### 2. Create Virtual Environment
```bash 
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
