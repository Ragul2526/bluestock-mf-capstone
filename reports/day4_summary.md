# Day 4 Summary - Performance Analytics

## Objective

The objective of Day 4 was to evaluate mutual fund performance using return, risk, risk-adjusted return, benchmark comparison, and composite ranking methodologies.

## Tasks Completed

### 1. Daily Return Analysis

* Computed daily returns for all 40 mutual fund schemes.
* Analyzed return distribution using histogram and QQ plot.
* Evaluated mean return, volatility, skewness, and extreme return behavior.

### 2. CAGR Analysis

* Calculated 1-year, 3-year, and 5-year CAGR for all schemes.
* Built a comparative performance table and visualized top-performing funds.

### 3. Sharpe Ratio Analysis

* Computed annualized Sharpe Ratio using a 6.5% risk-free rate.
* Ranked all schemes based on risk-adjusted returns.
* Identified top-performing funds on a volatility-adjusted basis.

### 4. Sortino Ratio Analysis

* Calculated annualized Sortino Ratio using downside deviation.
* Compared Sharpe and Sortino metrics across schemes.
* Evaluated downside-risk-adjusted performance.

### 5. Alpha and Beta Analysis

* Performed OLS regression of fund returns against NIFTY100 benchmark returns.
* Computed Alpha, Beta, R², and p-values for all schemes.
* Generated Alpha vs Beta visualization and exported results.

### 6. Maximum Drawdown Analysis

* Calculated maximum drawdown for all schemes.
* Identified peak-to-trough periods and drawdown durations.
* Ranked funds by downside risk.

### 7. Composite Fund Scorecard

* Developed a 0-100 scoring framework based on:

  * 30% 3-Year Return Rank
  * 25% Sharpe Ratio Rank
  * 20% Alpha Rank
  * 15% Expense Ratio Rank (Inverse)
  * 10% Maximum Drawdown Rank (Inverse)
* Ranked all schemes and identified top overall performers.

### 8. Benchmark Comparison

* Compared top 5 ranked funds against NIFTY50 and NIFTY100 benchmarks.
* Created normalized growth comparison chart over a 3-year period.

### 9. Tracking Error Analysis

* Computed annualized tracking error relative to NIFTY100.
* Evaluated benchmark deviation and active management characteristics.

## Key Findings

* Mirae Asset Large Cap Fund achieved the highest composite score.
* Large-cap and flexi-cap funds delivered the most balanced risk-return profiles.
* Small-cap funds generated strong returns but experienced significantly larger drawdowns.
* Top-performing schemes consistently ranked highly across CAGR, Sharpe Ratio, and composite scorecard metrics.
* Tracking errors indicated meaningful active management among leading schemes.

## Deliverables Generated

* Performance_Analytics.ipynb
* fund_scorecard.csv
* alpha_beta.csv
* benchmark_comparison.png
* CAGR comparison charts
* Sharpe Ratio analysis charts
* Sortino Ratio analysis charts
* Maximum Drawdown analysis charts
* Fund Scorecard visualization

## Status

Day 4 Performance Analytics completed successfully. All required calculations, visualizations, rankings, and deliverables were generated and validated.
