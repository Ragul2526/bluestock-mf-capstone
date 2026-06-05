# Bluestock Mutual Fund Capstone

## Day 1

- Project structure created
- Dependencies configured
- Data ingestion completed
- NAV API integration completed
- Fund master exploration completed
- AMFI validation completed

---

## Day 2 — Data Cleaning & SQLite

- Cleaned and validated 9 datasets — 0 duplicate or invalid records across core tables
- Retained 12 NULL values in yoy_growth_pct (no prior-year data available)
- Built bluestock_mf.db SQLite database with star schema (2 dims, 4 facts)
- Loaded 46,000+ NAV records, 32,778 transactions, verified all row counts
- Wrote and executed 10 analytical SQL queries

---

### Day 3 — Exploratory Data Analysis
- Produced 15 charts across Plotly, Seaborn, and Matplotlib
- Documented 10 key EDA insights as Markdown cells in the notebook
- Exported all charts as PNGs to `charts/`

Key findings:
- SBI MF leads AUM at ₹12.5L Cr — ~30% ahead of ICICI Prudential
- SIP inflows hit an all-time high of ₹31,002 Cr in December 2025
- Industry folios doubled from 13.26 Cr → 26.12 Cr (Jan 2022 – Dec 2025), CAGR ~18.5%
- Banking and IT dominate equity fund sector allocation
- T30 cities contribute ~66% of SIP inflows; B30 cities at 34% show growing penetration

---

### Day 4 — Performance Analytics

* Computed daily returns for all 40 mutual fund schemes
* Analyzed return distribution using histogram and QQ plot
* Calculated 1-year, 3-year, and 5-year CAGR across all funds
* Computed annualized Sharpe Ratio using 6.5% risk-free rate
* Computed annualized Sortino Ratio using downside deviation
* Performed Alpha-Beta regression against NIFTY100 benchmark
* Calculated Maximum Drawdown and drawdown duration for all schemes
* Built a composite Fund Scorecard (0–100) using:

  * 30% 3-Year Return Rank
  * 25% Sharpe Ratio Rank
  * 20% Alpha Rank
  * 15% Expense Ratio Rank (Inverse)
  * 10% Maximum Drawdown Rank (Inverse)
* Compared top 5 ranked funds against NIFTY50 and NIFTY100 benchmarks
* Computed annualized Tracking Error relative to NIFTY100

Key findings:

* Mirae Asset Large Cap Fund achieved the highest composite score (88.1)
* Large-cap and flexi-cap funds delivered the strongest risk-adjusted performance
* Small-cap funds generated higher returns but experienced significantly deeper drawdowns
* Top-performing schemes consistently ranked highly across CAGR, Sharpe Ratio, and composite scorecard metrics
* Tracking errors ranged from 18.8% to 21.7%, indicating meaningful active management

---

## Stack

| Purpose | Tools |
|---------|-------|
| Data manipulation | Python, Pandas, NumPy |
| Interactive charts | Plotly, Kaleido |
| Statistical charts | Seaborn |
| Base plotting | Matplotlib |
| Database | SQLite |
| Notebook | Jupyter |

---
