# FINRA CAT 2E Error Tracker

A simplified version of an automated tracking system I developed at Bank of America to monitor, document, and resolve FINRA CAT 2E regulatory errors. This project showcases how I used Excel macros, Python scripting, and process documentation to improve data accuracy, reduce turnaround time, and maintain compliance.

---

## Project Overview

FINRA’s Consolidated Audit Trail (CAT) requires firms to report trading activity with strict accuracy and within a 2.5-day window. To ensure compliance, I built a system to:

- Extract and track daily CAT 2E error data from FINRA’s CAIS portal
- Document root causes, responsible teams, and resolution progress
- Generate daily packages and email summaries for tech leads and executives
- Use macros and Python to automate key parts of the error lifecycle
- Provide real-time metrics (error rates, severity, resolution time) to help reduce error rates below 0.05%

---

## Tools & Technologies Used

- **Excel Macros (VBA)** — to automate tracker updates and reporting
- **Python** — for formatting, parsing portal exports, and cleanup
- **JIRA** — error log tracking and lifecycle documentation
- **Power BI / Excel Charts** — visualization of key metrics
- **Cesium ➝ ARC ➝ FINRA pipeline** — tracked data lineage and transformation

---

## What's Included (Sanitized for Demo)

| File | Description |
|------|-------------|
| sample_error_tracker.xlsx | Mock version of the Excel file used for error logging |
| generate_summary_email.py | Sample Python script to format errors into a daily summary |
| README.md | Overview of the project |
| data_flow_diagram.md | Simplified data flow: Cesium ➝ ARC ➝ FINRA |
| mock_error_data.csv | Example of anonymized daily error data used for demos |

---

## Key Metrics Tracked

- Total Errors by Severity Level
- Resolution Time (Per Team)
- Root Cause Categories
- Open vs. Closed Errors
- Error Rate Over Time (% of Total Records)

---

## Impact

- Reduced error rates to consistently below 0.05% (vs. national average of 1–2%)
- Streamlined communication between tech, operations, and compliance teams
- Improved executive visibility into risk and error trends
- Supported audit readiness with end-to-end traceability and documentation

---

## Lessons Learned

- Automating error lifecycle tracking saves hours weekly and improves accountability
- Clean documentation and visuals help non-technical stakeholders understand root cause trends
- Real-time dashboards drive faster, more informed decision-making

---

## Disclaimer

All sample data in this repository is fake and for illustrative purposes only. No proprietary or confidential information is shared.
