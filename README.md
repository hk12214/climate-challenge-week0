# Climate Change Analysis - Week 0
Analysis of climate trends in Africa (Ethiopia, Kenya, etc.) for COP32.

## How to Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Install tools: `pip install -r requirements.txt`
### References & Self-Learning
- **WMO State of the Climate in Africa 2024:** Used to define baseline periods for anomaly detection.
- **World Bank Climate Risk Profiles:** Guided the selection of KPI thresholds (e.g., extreme heat at >35°C).
- **Pandas Documentation:** Researched the deprecation of the 'M' offset in favor of 'ME' for time-series resampling in Python 3.15.