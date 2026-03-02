# Payments Business KPI Reporting Simulation

## Overview
This project simulates a commercial payments portfolio and builds a structured KPI reporting system to track financial and operational performance.

## Business Objective
To simulate how a payments business monitors revenue growth, cost efficiency, budget variance, regional performance, and operational KPIs.

## Key Metrics
- Revenue Growth (MoM & QoQ)
- Cost-to-Income Ratio
- Chargeback Rate
- Budget Variance
- Regional Contribution
- Top Underperforming Merchants
- SLA Alerts

## Project Structure
src/generate_merchant_data.py → Synthetic data generator  
src/kpi_engine.py → KPI reporting engine  
tests/test_validation.py → Basic validation test  

## How to Run
Generate data:
python src/generate_merchant_data.py

Run KPI engine:
python src/kpi_engine.py

Outputs are generated in the reports/ folder.

This project simulates real-world operational reporting workflows commonly used in payments and commercial banking environments.
