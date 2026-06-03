# Day 2 Data Cleaning & SQLite Summary

## 02_nav_history.csv

* Parsed date column successfully.
* Sorted records by amfi_code and date.
* Checked for duplicate records (0 found).
* Checked for missing NAV values (0 found).
* Checked for invalid NAV values <= 0 (0 found).

Conclusion:
The NAV history dataset was already clean and required only standard preprocessing and validation.

## 08_investor_transactions.csv

* Parsed transaction_date column.
* Validated transaction amounts.
* Checked transaction types (SIP, Lumpsum, Redemption).
* Checked KYC status values.
* Duplicate records found: 0.
* Invalid transaction amounts found: 0.

Conclusion:
Investor transaction data passed all validation checks.

## 07_scheme_performance.csv

* Validated performance metrics.
* Checked expense ratio range (0.1% - 2.5%).
* Duplicate records found: 0.
* Missing values found: 0.

Conclusion:
Scheme performance dataset was clean and required no corrective actions.

## 04_monthly_sip_inflows.csv

* Checked for missing values.
* Found 12 missing values in yoy_growth_pct.

Observation:
Missing values correspond to periods where prior-year comparison data was unavailable. Values were retained as NULL.

## Remaining Datasets

The following datasets underwent standard validation:

* 01_fund_master.csv
* 03_aum_by_fund_house.csv
* 05_category_inflows.csv
* 06_industry_folio_count.csv
* 09_portfolio_holdings.csv
* 10_benchmark_indices.csv

Validation performed:

* Duplicate check
* Missing value check
* Column consistency check

No significant data quality issues were identified.

## SQLite Database

Created SQLite database:

bluestock_mf.db

Tables loaded:

* dim_fund
* dim_date
* fact_nav
* fact_transactions
* fact_performance
* fact_aum

Row Counts:

* dim_fund: 40
* fact_nav: 46,000
* fact_aum: 90
* fact_performance: 40
* fact_transactions: 32,778
* dim_date: 1,150

All row counts matched the source CSV files.

## SQL Query Validation

10 analytical SQL queries were created and executed successfully.

Examples include:

* Top 5 funds by AUM
* Average NAV per month
* Monthly SIP analysis
* Transactions by state
* Funds with expense ratio below 1%
* Performance and risk analysis queries

## Conclusion

All datasets were cleaned and validated successfully. The cleaned data was loaded into SQLite, row counts were verified, and analytical SQL queries were executed successfully.
