# Listing changes
from original bkalil7/tcc

`requirements.txt` has all libraries needed to run distance and cointegration codes

## Measuring risk adjusted performance (task 4)

Added `risk_adjusted_performance/` directory.
<br>`risk_adjusted_analysis.ipynb`: notebook with draft to calculate measeures and view dataframe with them calculated per semester
<br>`risk_adjusted_performance.py`: code to calculate risk adjusted measures based on results:
- Outputs `distance_results/distance_risk_adjusted_measures.csv`
- Outputs `cointegration_results/cointegration_risk_adjusted_measures.csv`


## Classify operations by subperiod crisis vs. non-crisis (task 5)

`distance_gatev_v2.py`

Differences from `distance_gatev.py`:
1. Fixed errors on writing results in `distance_results/`
2. Added "Count day" into big_loop while statement, when it appends to the operation.csv file, using `counter` variable:

```python
operations.append({
    "Semester": big_loop,
    "Days": counter_ret,
    "S1": pairs[p]['s1_ticker'],
    "S2": pairs[p]['s2_ticker'],
    "Pair": f"{pairs[p]['s1_ticker']}-{pairs[p]['s2_ticker']}",
    "Return": Rcum_ret[-1],
    "Converged": converged,
    "Count day": counter # here is the line I added
    })
```

### Directory `crisis_analysis/`

Created directory
<br> Added `bear_markets.csv` file with periods of bear markets in histort, based on Hartford Funds reseach
<br> Added `crisis_analysis.ipynb` notebook to do data manipulation, later incorporated on `operations_crisis_classification.py`
    
`distance_code/operations_crisis_classification.py`
- Added this .py script classifying operations from pairs trading into bear market period
- Outputs `distance_results/operations_crisis_classified.csv`
- Outputs `cointegration_results/operations_crisis_classified.csv`
        
Additional files for support:        
- Outputs `distance_data/period_crisis_classification.csv`
- Outputs `cointegration_data/period_crisis_classification.csv`