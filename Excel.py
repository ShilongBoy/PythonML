from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
#Load boston housing dataset as an example
boston = load_boston()

df = pd.read_csv("C:/Users/user/Desktop/POC/ZbankPOC_Test_SZ2.csv",error_bad_lines=False)
dy=df[df.columns[0]]
dx=df[df.columns[1:]]
X = boston["data"]
Y = boston["target"]
names = ['x1','x2','x3','x4','x5']
print("names:",names)
rf = RandomForestRegressor(n_estimators=20, max_depth=4)
scores = []
for i in range(dx.shape[1]):
     score = cross_val_score(rf, dx[:, i:i+1], dy, scoring="r2",
                              cv=ShuffleSplit(len(dx), 3, .3))
     scores.append((round(np.mean(score), 3), names[i]))
print(sorted(scores, reverse=True))