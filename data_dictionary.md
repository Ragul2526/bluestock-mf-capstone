# Data Dictionary

## dim_fund

| Column       | Data Type | Business Definition                | Source             |
| ------------ | --------- | ---------------------------------- | ------------------ |
| amfi_code    | INTEGER   | Unique AMFI scheme identifier      | 01_fund_master.csv |
| fund_house   | TEXT      | Mutual fund company name           | 01_fund_master.csv |
| scheme_name  | TEXT      | Name of mutual fund scheme         | 01_fund_master.csv |
| category     | TEXT      | Fund category (Equity, Debt, etc.) | 01_fund_master.csv |
| sub_category | TEXT      | Detailed scheme classification     | 01_fund_master.csv |

---

## dim_date

| Column     | Data Type | Business Definition | Source                   |
| ---------- | --------- | ------------------- | ------------------------ |
| date       | DATE      | Calendar date       | Derived from NAV history |
| year       | INTEGER   | Year component      | Derived                  |
| month      | INTEGER   | Month component     | Derived                  |
| month_name | TEXT      | Month name          | Derived                  |
| quarter    | INTEGER   | Calendar quarter    | Derived                  |

---

## fact_nav

| Column    | Data Type | Business Definition           | Source             |
| --------- | --------- | ----------------------------- | ------------------ |
| amfi_code | INTEGER   | Scheme identifier             | 02_nav_history.csv |
| date      | DATE      | NAV observation date          | 02_nav_history.csv |
| nav       | REAL      | Net Asset Value of the scheme | 02_nav_history.csv |

---

## fact_transactions

| Column           | Data Type | Business Definition              | Source                       |
| ---------------- | --------- | -------------------------------- | ---------------------------- |
| investor_id      | TEXT      | Investor identifier              | 08_investor_transactions.csv |
| transaction_date | DATE      | Transaction date                 | 08_investor_transactions.csv |
| amfi_code        | INTEGER   | Scheme identifier                | 08_investor_transactions.csv |
| transaction_type | TEXT      | SIP, Lumpsum, Redemption         | 08_investor_transactions.csv |
| amount_inr       | REAL      | Transaction amount in INR        | 08_investor_transactions.csv |
| state            | TEXT      | Investor state                   | 08_investor_transactions.csv |
| city             | TEXT      | Investor city                    | 08_investor_transactions.csv |
| kyc_status       | TEXT      | Investor KYC verification status | 08_investor_transactions.csv |

---

## fact_performance

| Column             | Data Type | Business Definition                  | Source                    |
| ------------------ | --------- | ------------------------------------ | ------------------------- |
| amfi_code          | INTEGER   | Scheme identifier                    | 07_scheme_performance.csv |
| return_1yr_pct     | REAL      | One-year return percentage           | 07_scheme_performance.csv |
| return_3yr_pct     | REAL      | Three-year return percentage         | 07_scheme_performance.csv |
| return_5yr_pct     | REAL      | Five-year return percentage          | 07_scheme_performance.csv |
| benchmark_3yr_pct  | REAL      | Benchmark return over three years    | 07_scheme_performance.csv |
| alpha              | REAL      | Risk-adjusted excess return          | 07_scheme_performance.csv |
| beta               | REAL      | Market sensitivity measure           | 07_scheme_performance.csv |
| sharpe_ratio       | REAL      | Risk-adjusted performance metric     | 07_scheme_performance.csv |
| sortino_ratio      | REAL      | Downside-risk adjusted return metric | 07_scheme_performance.csv |
| std_dev_ann_pct    | REAL      | Annualized volatility                | 07_scheme_performance.csv |
| max_drawdown_pct   | REAL      | Maximum observed decline             | 07_scheme_performance.csv |
| aum_crore          | REAL      | Assets under management (crore INR)  | 07_scheme_performance.csv |
| expense_ratio_pct  | REAL      | Annual expense ratio percentage      | 07_scheme_performance.csv |
| morningstar_rating | INTEGER   | Morningstar fund rating              | 07_scheme_performance.csv |
| risk_grade         | TEXT      | Risk classification                  | 07_scheme_performance.csv |

---

## fact_aum

| Column         | Data Type | Business Definition      | Source                   |
| -------------- | --------- | ------------------------ | ------------------------ |
| date           | DATE      | Observation date         | 03_aum_by_fund_house.csv |
| fund_house     | TEXT      | Mutual fund company      | 03_aum_by_fund_house.csv |
| aum_lakh_crore | REAL      | AUM in lakh crore INR    | 03_aum_by_fund_house.csv |
| aum_crore      | REAL      | AUM in crore INR         | 03_aum_by_fund_house.csv |
| num_schemes    | INTEGER   | Number of active schemes | 03_aum_by_fund_house.csv |

---

## Database Relationships

* dim_fund.amfi_code → fact_nav.amfi_code
* dim_fund.amfi_code → fact_transactions.amfi_code
* dim_fund.amfi_code → fact_performance.amfi_code

## Database

Database Name: bluestock_mf.db

Database Type: SQLite

Schema Type: Star Schema
