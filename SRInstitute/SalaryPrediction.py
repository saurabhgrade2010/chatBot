import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def myprediction(num):
    dataset = pd.read_csv("Salary_Data.csv")
    X= dataset.iloc[:, :-1].values
    y= dataset.iloc[:, 1].values
    regressor = LinearRegression()
    regressor.fit(X,y)
    t=[[num]]
    y_pred = regressor.predict(t)
    x=float(y_pred)
    return float("{:.2f}".format(x))