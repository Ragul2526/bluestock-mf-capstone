# Day 1 Data Quality Summary

## Fund Master Exploration

Unique Fund Houses: 10

Categories:

* Equity
* Debt

Sub-Categories:

* Large Cap
* Small Cap
* Gilt
* Mid Cap
* Short Duration
* Value
* Liquid
* Index/ETF
* Flexi Cap
* Index
* Large & Mid Cap
* ELSS

Risk Categories:

* Low
* Moderate
* Moderately High
* High
* Very High

## AMFI Code Validation

Validation was performed between `fund_master.csv` and `nav_history.csv`.

Result:

* Missing Codes: 0
* Validation Passed: True

All AMFI scheme codes present in the fund master dataset have corresponding records in the NAV history dataset.

## API Observation

The MFAPI endpoint successfully returned NAV and metadata for all supplied scheme codes.

However, several scheme codes currently map to different scheme names than those specified in the assignment description it was found by checking the metadata which is saved to data/raw as well for better understanding. The implementation uses the assignment-provided scheme codes and records the metadata returned by MFAPI.