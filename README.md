# Bluestock Mutual Fund Capstone

## Day 1

- Project structure created
- Dependencies configured
- Data ingestion completed
- NAV API integration completed
- Fund master exploration completed
- AMFI validation completed

## Day 2 — Data Cleaning & SQLite

- Cleaned and validated 9 datasets — 0 duplicate or invalid records across core tables
- Retained 12 NULL values in yoy_growth_pct (no prior-year data available)
- Built bluestock_mf.db SQLite database with star schema (2 dims, 4 facts)
- Loaded 46,000+ NAV records, 32,778 transactions, verified all row counts
- Wrote and executed 10 analytical SQL queries

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

