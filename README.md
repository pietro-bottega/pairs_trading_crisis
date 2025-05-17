# Listing changes
from original bkalil7/tcc

## Approach 1

Classify operations (final result) by crisis period

`distance_gatev_v2.py`

    Difference from `distance_gatev.py`:
    1. Fixed errors on writing results in `distance_results/`
    2. Added "Count day" into big_loop while statement, when it appends to the operation.csv file, using `counter` variable

`crisis_analysis/`

    Created directory
    Added `bear_markets.csv` file with periods of bear markets in histort, based on Hartford Funds reseach
    Added `crisis_analysis.ipynb` notebook to do data manipulation, later incorporated on `operations_crisis_classification.py`
    
    `distance_code/operations_crisis_classification.py`
        Added this .py script classifying operations from pairs trading into bear market period
        Outputs `distance_results/operations_crisis_classified.csv`
        Outputs `cointegration_results/operations_crisis_classified.csv`
        
        To be used in approach 2:
        Outputs `distance_data/period_crisis_classification.csv`
        Outputs `cointegration_data/period_crisis_classification.csv`