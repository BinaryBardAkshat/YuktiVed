# yuktived/stats.py

import numpy as np

def mean(series):
    return np.mean(series.data)

def median(series):
    return np.median(series.data)

def std(series):
    return np.std(series.data)

def correlation(series1, series2):
    return np.corrcoef(series1.data, series2.data)

def hypothesis_test(dataframe, hypothesis):
 
    return None


