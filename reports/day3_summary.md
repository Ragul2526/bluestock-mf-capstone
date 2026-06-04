# Day 3 - Exploratory Data Analysis (EDA) Summary

## Objective

Perform comprehensive exploratory data analysis on the mutual fund ecosystem datasets
to uncover trends, patterns, and relationships across NAV history, AUM, SIP inflows,
investor demographics, folio counts, and portfolio holdings.

## Charts Produced (15 Total)

| # | Chart | Library | File |
|---|-------|---------|------|
| 1 | Daily NAV Trend 2022–2026 with Bull Run & Correction highlights | Plotly | nav_trend.png |
| 2 | AUM Growth by Fund House 2022–2025 (grouped bar) | Seaborn | aum_growth.png |
| 3 | Top Fund Houses by Latest AUM | Seaborn | top_fund_houses.png |
| 4 | Monthly SIP Inflow Trend with ₹31,002 Cr ATH annotation | Plotly | sip_inflow.png |
| 5 | Category Inflow Heatmap (months × categories) | Seaborn | category_heatmap.png |
| 6 | Investor Age Group Distribution (pie) | Matplotlib | age_group_distribution.png |
| 7 | SIP Amount by Age Group (box plot) | Seaborn | sip_boxplot_age.png |
| 8 | Gender Distribution (pie) | Matplotlib | gender_distribution.png |
| 9 | Total SIP Amount by State (horizontal bar) | Matplotlib | sip_by_state.png |
| 10 | T30 vs B30 City Tier Distribution (pie) | Matplotlib | t30_b30_distribution.png |
| 11 | Industry Folio Growth 2022–2025 with milestones | Matplotlib | folio_growth.png |
| 12 | NAV Return Correlation Matrix — 10 funds | Seaborn | nav_correlation_heatmap.png |
| 13 | Sector Allocation Donut | Plotly | sector_donut.png |
| 14 | Top 10 Sectors by Portfolio Weight | Seaborn | top_sectors.png |
| 15 | Top 10 States by Investment Amount | Seaborn | top_states.png |

## Key EDA Findings

1. **NAV Trends:** Equity fund NAVs showed a broad-based bull run through 2023
   (20–35% gains across schemes), followed by intermittent corrections in 2024.

2. **AUM Dominance:** SBI Mutual Fund led all fund houses at ₹12.5L Cr AUM in 2025,
   approximately 30% ahead of ICICI Prudential, with all 10 fund houses showing
   consistent year-on-year growth.

3. **SIP All-Time High:** Monthly SIP inflows reached a record ₹31,002 Cr in
   December 2025, reflecting structural retail participation independent of
   market cycles.

4. **Category Inflows:** Large-cap and flexi-cap categories attracted the most
   consistent net inflows; sectoral/thematic funds showed spiky, event-driven
   inflow patterns.

5. **Investor Age Profile:** The 25–40 age band constitutes the largest SIP
   participant group, with median SIP amounts rising progressively with age.

6. **Gender Split:** Male investors hold the majority of folios, though female
   investor growth has accelerated post-2023, indicating improving financial
   inclusion.

7. **Geographic Distribution:** Punjab and Tamil Nadu lead in total SIP amounts;
   T30 cities contribute ~66% of inflows while B30 cities account for a meaningful
   34%, showing steady geographic democratisation.

8. **Folio Growth:** Total industry folios doubled from 13.26 Cr (Jan 2022) to
   26.12 Cr (Dec 2025), a CAGR of ~18.5%, with growth sustained even during
   volatile market phases.

9. **Return Correlations:** The 10 selected funds showed near-zero pairwise return
   correlations (all off-diagonal values < 0.1), confirming they span diverse
   categories and offer strong diversification potential.

10. **Sector Allocation:** Banking is the largest single sector in aggregate equity
    fund portfolios, followed by IT — together reflecting the index-heavy tilt of
    Indian mutual funds toward financials and technology.

## Data Quality Notes

- NAV chart uses `amfi_code` as color identifier (scheme name mapping pending).
- Category heatmap columns formatted to `Mon YYYY` for readability.
- AUM bar chart confidence interval error bars removed (`errorbar=None`) as values
  represent actuals, not statistical estimates.
- 12 missing values in `yoy_growth_pct` (SIP inflows) retained as NULL —
  correspond to periods with no prior-year comparison data (carried forward from Day 2).

## Deliverables

- `EDA_Analysis.ipynb` — notebook with 15 charts and 10 Markdown insight cells
- `charts/` — 15 exported PNG files for final report

## Tools Used

- Python, Pandas, NumPy
- Plotly (interactive charts: NAV trend, SIP inflow, sector donut)
- Seaborn (statistical charts: AUM grouped bar, heatmap, correlation matrix, box plot)
- Matplotlib (distribution charts: pie charts, folio growth, state bar)
- Kaleido (Plotly PNG export)