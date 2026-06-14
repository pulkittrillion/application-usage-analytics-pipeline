# Application Usage Analytics Pipeline

**End-to-end ETL pipeline** to analyze application usage data and track automation adoption metrics — directly inspired by real enterprise operations (18% → 99% adoption).

## Business Problem
Tracking application adoption vs manual work was previously done manually in Excel. This pipeline automates the process and delivers key business metrics.

## Tech Stack
- Python, Pandas
- PostgreSQL
- psycopg2

## Pipeline Flow
1. **Extract** — Raw usage logs from CSV
2. **Transform** — Calculate adoption rate, manual rate, efficiency score, categorization
3. **Load** — Store in PostgreSQL for analysis

## How to Run

```bash
pip install -r requirements.txt
python run_pipeline.py