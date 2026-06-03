from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
import pandas as pd
pd.set_option('display.max_columns', None)
#02_nav_history.csv


print("Reading 02_nav_history.csv")
nav = pd.read_csv( BASE_DIR / "data" / "raw" / "02_nav_history.csv")
original_rows = len(nav)
print("Missing NAV values:",nav["nav"].isna().sum())
nav["date"] = pd.to_datetime(nav["date"]) # parsing dates, already in ISO format
nav = nav.sort_values(["amfi_code", "date"]) # sorting by amfi_code and date
nav = nav.drop_duplicates() # removing duplicate values
nav = nav[nav["nav"] > 0] # keeping valid nav only(values above 0)
print("Rows before cleaning:", original_rows)
print("Rows after cleaning:", len(nav))
nav.to_csv(BASE_DIR / "data" / "processed"/"02_nav_history_clean.csv",index=False)
print("Cleaning is done for 02_nav_history.csv and saved in data/processed/02_nav_history_clean.csv")


#08_investor_transactions_clean.csv


print("Reading 08_investor_transactions.csv")
investor_tr = pd.read_csv(BASE_DIR / "data" / "raw" / "08_investor_transactions.csv")
investor_tr["transaction_date"] = pd.to_datetime(investor_tr["transaction_date"])
print("Missing values:\n",investor_tr.isnull().sum())
print("Invalid amounts:", (investor_tr["amount_inr"] <= 0).sum())
print("Duplicates:", investor_tr.duplicated().sum())
print("Unique AMFI Codes:", investor_tr["amfi_code"].nunique())
investor_tr.to_csv(BASE_DIR / "data" / "processed" / "08_investor_transactions_clean.csv",index=False)


#07_scheme_performance.csv


print("Reading 07_scheme_performance.csv")
scheme_per = pd.read_csv(BASE_DIR / "data" / "raw" / "07_scheme_performance.csv")
#print(scheme_per.columns) 
print("Missing values : \n", scheme_per.isnull().sum())
print(scheme_per.describe())
invalid_expense = scheme_per[(scheme_per["expense_ratio_pct"] < 0.1) | (scheme_per["expense_ratio_pct"] > 2.5)]
print("Invalid expense ratios:", len(invalid_expense))
print("Duplicates:", scheme_per.duplicated().sum())
scheme_per.to_csv(BASE_DIR / "data" / "processed" / "07_scheme_performance_clean.csv",index=False)


#Rest of the 7 files cleaning

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(BASE_DIR / "data" / "raw" /f"{file}")

    print("\n" + "="*60)
    print(file)

    print("Shape:", df.shape)

    print("Duplicates:", df.duplicated().sum())

    print("Missing Values:")
    print(df.isnull().sum())
    name = os.path.splitext(file)[0]
    df.to_csv(BASE_DIR / "data" / "processed" / f"{name}_clean.csv", index = False)