# Adding indicator of crisis periods in the operations.csv

import pandas as pd
import numpy as np
from pandas.tseries.offsets import *
from pandas.tseries.holiday import USFederalHolidayCalendar

# IMPORTING FILES

## Bear market historical classification

bear_markets = pd.read_csv("../crisis_analysis/bear_markets.csv") # read file listing bear market periods in history
bear_markets = bear_markets.drop(columns=['return_percentage','days_duration'])

type_mapping = {
    'start': 'datetime64[ns]',
    'end': 'datetime64[ns]'
}

bear_markets = bear_markets.astype(type_mapping) # ensure dtype is datetime

## Operations from distance

distance_operations = pd.read_csv("../distance_results/operations.csv").drop(columns=['Unnamed: 0'])

## Operations from cointegrations

########################################################

# FUNCTIONS

def create_daily_bear_market_indicator(bear_markets):
    '''
    Transform a dataframe of bear market start and end dates into a daily time series
    with an indicator for whether each date is in a bear market.
    
    Parameters:
    -----------
    bear_periods_df : pandas.DataFrame
        DataFrame with 'start' and 'end' columns containing dates of bear market periods
    
    Returns:
    --------
    pandas.DataFrame
        Daily time series with columns 'date' and 'is_bear_market'
    '''
    
    min_date = bear_markets['start'].min()
    max_date = bear_markets['end'].max()
    
    date_range = pd.date_range(start=min_date, end=max_date, freq='D')
    daily_df = pd.DataFrame({'date': date_range})
    
    daily_df['is_bear_market'] = 0
    
    for _, row in bear_markets.iterrows():
        mask = (daily_df['date'] >= row['start']) & (daily_df['date'] <= row['end'])
        daily_df.loc[mask, 'is_bear_market'] = 1
        
    return daily_df

def list_business_days(start_date, end_date):
    '''
    Create a list of business days between a date range, excludes US Federal Holidays

    Parameters:
    ----------
    start_date : datetime
    end_date : datetime
        start and end dates for the dataframe to be created.

    Returns:
    --------
    series
        Series of business days between date range.
    '''
    us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
    date_range = pd.date_range(start=start_date, end=end_date, freq=us_bd)
    return [date.date() for date in date_range]


# DATA MANIPULATION

daily_bear_market = create_daily_bear_market_indicator(bear_markets) # Applying function to turn list of bear market periods to a complete list of dates classified

start_date = '1990-01-01' # first date from dataset
end_date = '2015-12-31' # last possible date from dataset
business_days = pd.DataFrame(list_business_days(start_date, end_date), columns=['date']).astype({'date': 'datetime64[ns]'})

analysis_period_classified = pd.merge( # creates a new dataframe listing dates present on original dataframe, classified in bear market periods
    left = business_days,
    right = daily_bear_market,
    left_on = 'date',
    right_on = 'date',
    how = 'inner'
).reset_index()

distance_operations_classified = pd.merge(
    left = distance_operations,
    right = analysis_period_classified,
    left_on = 'Count day',
    right_on = 'index',
    how = 'left'
).drop(columns=['index'])

# OUTPUTTING FILES

analysis_period_classified.to_csv(f"../distance_data/period_crisis_classification.csv")
analysis_period_classified.to_csv(f"../cointegration_data/period_crisis_classification.csv")

distance_operations.to_csv(f"../distance_results/operations_crisis_classified.csv")

######################################################## cointegration_operations