import pandas
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler

import numpy as np
import pickle

dataset = pandas.read_csv("random_eval_transformed.csv", dtype=np.intc)
# Split the dataset into training and testing
dataset = pandas.DataFrame(StandardScaler().fit_transform(dataset))

X = dataset[dataset.columns[1:]]
Y = dataset[dataset.columns[0]]

print("Splitting data")
XTrain, XTest, yTrain, yTest = train_test_split(X, Y, test_size=0.2, random_state=42)
print("Finish")

print("Training")
reg = HistGradientBoostingRegressor(early_stopping=True, l2_regularization=0.3,
                              max_iter=300, max_leaf_nodes=None, verbose=3)
print(reg)
reg.fit(XTrain, yTrain)
print("Score: ", reg.score(XTest, yTest))
print("MSE: ", mean_squared_error(yTest, reg.predict(XTest)))
print("MAE: ", mean_absolute_error(yTest, reg.predict(XTest)))

with open('hist.sav', 'wb') as f:
    pickle.dump(reg, f)
print("Done")