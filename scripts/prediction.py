#!/usr/bin/env python3

# import packages
import pandas as pd
from sklearn.linear_model import LinearRegression

# load mtcars dataset
mtcars = pd.read_csv("scripts/mtcars.csv")

# select only continuous variables
relevant_cols = ['cyl', 'disp', 'hp', 'drat', 'wt', 'qsec']
x_train = mtcars[relevant_cols]

# use MPG as output variable
y_train = mtcars['mpg']

# build linear model
model_mpg = LinearRegression().fit(x_train, y_train)

# create prediction result
def predict(json_dict):
    df = pd.DataFrame(json_dict, index=[0])
    x = df[relevant_cols]
    res = model_mpg.predict(x)
    return res[0]