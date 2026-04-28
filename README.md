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