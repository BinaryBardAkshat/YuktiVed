# yuktived/ml.py

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier

class SklearnLinearRegression:
    def __init__(self, fit_intercept=True):
        self.model = LinearRegression(fit_intercept=fit_intercept)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

class SklearnLogisticRegression:
    def __init__(self, fit_intercept=True):
        self.model = LogisticRegression(fit_intercept=fit_intercept)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

class SklearnDecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.model = DecisionTreeClassifier(max_depth=max_depth)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)


