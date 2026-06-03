CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
fund_house TEXT,
scheme_name TEXT,
category TEXT,
sub_category TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT UNIQUE,
year INTEGER,
month INTEGER,
month_name TEXT,
quarter INTEGER
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
date TEXT,
nav REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
transaction_date TEXT,
amfi_code INTEGER,
transaction_type TEXT,
amount_inr REAL,
state TEXT,
city TEXT,
kyc_status TEXT,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    aum_crore REAL,
    expense_ratio_pct REAL,
    morningstar_rating INTEGER,
    risk_grade TEXT,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
fund_house TEXT,
aum_lakh_crore REAL,
aum_crore REAL,
num_schemes INTEGER
);
