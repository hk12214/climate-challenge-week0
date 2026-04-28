# African Climate Trend Analysis - Week 0

This project focuses on analyzing historical climate data from Ethiopia, Kenya, Sudan, Tanzania, and Nigeria (2015–2026) to support Ethiopia's position for COP32.

## ## 1. Business Objective: The Three-Layer Framework
To align with the project goals for the COP32 position paper, our analysis operates across three distinct layers:

1.  **Layer 1: Climate Feature Analysis (Data Layer)**
    * *Objective:* Extract high-fidelity trends from NASA meteorological data (Temperature, Precipitation, Humidity).
    * *Action:* Cleaning, normalization, and outlier detection across five target countries.
2.  **Layer 2: Regional Impact Mapping (Analytical Layer)**
    * *Objective:* Translate raw data into specific regional "signals" (e.g., Sahelian heat vs. Tropical monsoon intensity).
    * *Action:* Identifying correlations like $QV2M$ vs. $T2M$ to predict future climate stressors.
3.  **Layer 3: Policy & Adaptation Strategy (Decision Layer)**
    * *Objective:* Convert insights into actionable policy recommendations for climate finance and "Loss and Damage" negotiations.

---

## ## 2. Project Structure

* **.github/workflows/:** CI/CD pipelines for automated testing and environment validation.
* **notebooks/:** Country-specific Jupyter notebooks for EDA and cross-country comparisons.
* **scripts/:** Modular Python scripts for data cleaning and statistical processing.
* **src/:** Core utility functions and reusable source code.
* **tests/:** Unit tests to ensure the integrity of the data processing pipeline.
* **data/:** (Local only) Directory for raw and cleaned datasets. *Note: This folder is git-ignored to prevent large file sync issues.*

## ## 3. Technical Setup & Environment

### ### Prerequisite: Git Configuration
To prevent `RPC failed (curl 55)` errors when pushing large notebooks, run the following command to increase your Git buffer:
```bash
git config --global http.postBuffer 524288000
  ```

## ## 4. Setup Instructions

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
```
### 4. Register Jupyter Kernel:
```bash 
python -m ipykernel install --user --name=venv --display-name "Python (Climate-Env)"
```
## ## 4. Version Control Strategy
* Branching: Features are developed in country-specific branches (e.g., eda-ethiopia) and comparative tasks in compare-countries.

* Cleanup: All notebook outputs must be cleared before committing to maintain repository efficiency.

* Merging: Features are merged into main only after passing baseline unit tests in the .github/workflows/.
## 🌍 Interactive Climate Dashboard (Bonus)
As part of the Decision Layer (Layer 3) of this project, an interactive dashboard was developed using Streamlit. This tool allows policy makers to visualize regional climate stressors in real-time, moving beyond static analysis.

### 🔗 Access & Deployment

Branch: dashboard-dev
#### ⚠️ Data Requirements (Local Run)
Note: The data/ folder is .gitignoreed to maintain repository efficiency. To run the dashboard locally:

1. Create Directory: Ensure a /data folder exists in the project root.

2. Add Files: Place your processed *_clean.csv files (from Task 2) inside that folder.

3. Run App: Execute streamlit run app/main.py from the root.

If the /data folder is empty, the app will trigger a "No objects to concatenate" error.

### 🛠️ Dashboard Architecture
The app follows a modular structure to ensure speed and interactivity:
* Reactive Filters: Users can filter the entire dataset by Country, Year Range, and Climate Variable ($T2M$, $PRECTOTCORR$, $RH2M$).
* Dynamic Visualizations: Powered by Plotly Express, providing interactive tooltips and zooming capabilities for time-series trends and distribution boxplots.
* Key Metrics: High-level KPIs that recalculate instantly based on user-selected filters, showing "Max Temperature" and "Average Rainfall" across selected regions.
![Dashboard Preaview](dashboard_screenshots/dashboard.png)

## References & Self-Learning
- **WMO State of the Climate in Africa 2024:** Used to define baseline periods for anomaly detection.
- **World Bank Climate Risk Profiles:** Guided the selection of KPI thresholds (e.g., extreme heat at >35°C).
- **Pandas Documentation:** Researched the deprecation of the 'M' offset in favor of 'ME' for time-series resampling in Python 3.15.
