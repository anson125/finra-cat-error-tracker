# Data Flow Diagram

**Data Lineage:**
Cesium ➝ ARC ➝ FINRA (CAT CAIS)

- Cesium: Receives and aggregates data from 6+ source systems.
- ARC: Transforms and maps Cesium data into JSON format for CAT submissions.
- FINRA: Final recipient for CAT 2E regulatory submissions and error reporting.
