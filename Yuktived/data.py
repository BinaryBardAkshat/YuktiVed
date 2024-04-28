# yuktived/data.py

import pandas as pd

class DataFrame:
    def __init__(self, data=None, index=None, columns=None):
        self.data = pd.DataFrame(data=data, index=index, columns=columns)

    def head(self, n=5):
        return self.data.head(n)

    def tail(self, n=5):
        return self.data.tail(n)

    def describe(self):
        return self.data.describe()

class Series:
    def __init__(self, data=None, index=None, name=None):
        self.data = pd.Series(data=data, index=index, name=name)

    def head(self, n=5):
        return self.data.head(n)

    def tail(self, n=5):
        return self.data.tail(n)

    def describe(self):
        return self.data.describe()

def read_csv(filename):
    return pd.read_csv(filename)

def read_excel(filename):
    return pd.read_excel(filename)

def to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)

def to_excel(dataframe, filename):
    dataframe.to_excel(filename, index=False)

def merge(dataframes, **kwargs):
    return pd.merge(*dataframes, **kwargs)

def groupby(dataframe, by):
    return dataframe.groupby(by)

