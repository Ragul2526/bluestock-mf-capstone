import pandas as pd
from pathlib import Path

fund_master = pd.read_csv(
    Path("../data/raw/01_fund_master.csv")
)

nav_history = pd.read_csv(
    Path("../data/raw/02_nav_history.csv")
)

print("Unique Fund Houses")
print(fund_master["fund_house"].unique())

print("\nCategories")
print(fund_master["category"].unique())

print("\nSub Categories")
print(fund_master["sub_category"].unique())

print("\nRisk Categories")
print(fund_master["risk_category"].unique())

master_codes = set(fund_master["amfi_code"])
history_codes = set(nav_history["amfi_code"])

missing = master_codes - history_codes

print("\nMissing Codes")
print(missing)

print("\nValidation Passed:", len(missing) == 0)