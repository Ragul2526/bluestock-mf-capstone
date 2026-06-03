-- 1. Top 5 Fund Houses by AUM

SELECT fund_house,MAX(aum_crore) AS aum_crore
FROM fact_aum
GROUP BY fund_house
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Month

SELECT substr(date,1,7) AS month,ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. Monthly SIP Collection

SELECT
    substr(transaction_date,1,7) AS month,
    ROUND(SUM(amount_inr),2) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY month
ORDER BY month;


-- 4. Transactions by State

SELECT state,COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;


-- 5. Funds with Expense Ratio below 1%

SELECT amfi_code,expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 10 Funds by 5-Year Return

SELECT scheme_name,return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 7. Highest Sharpe Ratio Funds

SELECT scheme_name,sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- 8. Average Transaction Amount by State

SELECT state,ROUND(AVG(amount_inr),2) AS avg_amount
FROM fact_transactions
GROUP BY state
ORDER BY avg_amount DESC;


-- 9. Total Transactions by Transaction Type

SELECT transaction_type,COUNT(*) AS total_transactions,ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 10. Top 10 Funds by AUM

SELECT fund_house,SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 10;