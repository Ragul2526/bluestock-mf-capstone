#Creating this file to show how  i have created the database
import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

conn = sqlite3.connect(
    BASE_DIR/"data/db/bluestock_mf.db"
)

# Load cleaned datasets
fund = pd.read_csv(BASE_DIR / "data/processed/01_fund_master_clean.csv")
nav = pd.read_csv(BASE_DIR / "data/processed/02_nav_history_clean.csv")
aum = pd.read_csv(BASE_DIR / "data/processed/03_aum_by_fund_house_clean.csv")
performance = pd.read_csv(BASE_DIR / "data/processed/07_scheme_performance_clean.csv")
transactions = pd.read_csv(BASE_DIR / "data/processed/08_investor_transactions_clean.csv")

# Create dim_date
dates = pd.DataFrame({
    "date": pd.to_datetime(nav["date"]).unique()
})

dates["year"] = dates["date"].dt.year
dates["month"] = dates["date"].dt.month
dates["month_name"] = dates["date"].dt.month_name()
dates["quarter"] = dates["date"].dt.quarter

# Load tables
fund.to_sql("dim_fund", conn, if_exists="replace", index=False)
nav.to_sql("fact_nav", conn, if_exists="replace", index=False)
aum.to_sql("fact_aum", conn, if_exists="replace", index=False)
performance.to_sql("fact_performance", conn, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", conn, if_exists="replace", index=False)
dates.to_sql("dim_date", conn, if_exists="replace", index=False)
conn.close()
# Verify row counts
print("\nRow Counts")
print("dim_fund:", len(fund))
print("fact_nav:", len(nav))
print("fact_aum:", len(aum))
print("fact_performance:", len(performance))
print("fact_transactions:", len(transactions))
print("dim_date:", len(dates))

print("\nDatabase created successfully")