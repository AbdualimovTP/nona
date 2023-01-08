"""
Author: Timur Pulatovich Abdualimov
Date code: 08.12.2023
"""


import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def nona(data, algreg = make_pipeline(StandardScaler(with_mean=False), Ridge(alpha=0.1)), algclass = RandomForestClassifier(max_depth=2, random_state=0)):

    """
    Missing value prediction function. We go through all the columns, identifying the column with missing values. We divide the sample into train and test. We predict missing values ​​using machine learning.
    Parameters:
        Data: prepared dataset
        algreg: Regression algorithm to predict missing values ​​in columns
        algclss: Classification algorithm to predict missing values ​​in columns
    """

    for i in tqdm(data.columns): # loop through all columns from first to last
        # if there are gaps in the first column, fill in the missing values with the median
        if i == data.columns[0] and data[i].isna().sum() != 0:
            data[i] = data[i].fillna(data[i].median())
            continue

        # check if there are gaps in the column, if there are - the algorithm works
        if data[i].isna().sum() != 0:
            indexna = data[data[i].isna()].index # display row indices in a column with gaps
            datanona = data.loc[:, data.isna().any()==False] # output columns without gaps
            X_train_nona = datanona.loc[datanona.index.isin(indexna) == False] # create a train sample for training, it includes only columns without gaps, perform fibration on the index of the test sample, leave only the columns in which we know the predicted value
            X_test_nona = datanona.loc[indexna] # create a test sample, leave the columns in which we do not know the predicted value
            y_train_nona = data[i].loc[datanona.index.isin(indexna) == False] # leave the values in the predicted column without gaps

            # if the predicted number is an integer and the number of predicted values is less than 20, we solve the classification
            if data[i].nunique() < 20 and float(data[i].unique()[~np.isnan (data[i].unique())][0]).is_integer():
                class_nona = algclass
                class_nona.fit(X_train_nona, y_train_nona)
                data.loc[data[i].isna(), i] = class_nona.predict(X_test_nona) # predict the values and insert them into the missing values in the column

            else:
                reg_nona = algreg
                reg_nona.fit(X_train_nona, y_train_nona)
                data.loc[data[i].isna(), i] = reg_nona.predict(X_test_nona) # predict the values and insert them into the missing values in the column
