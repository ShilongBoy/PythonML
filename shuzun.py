# -*- coding:utf-8 -*-
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.linear_model import LogisticRegression

def loadDataSet():
    dataMat=[]
    dataLab=[]
    lines=open('D:/soft/python/testLR_Test.txt')
    for i in lines.readline():
        values=i.split("    ")
        dataMat.append(float(values[0]),float(values[1]))
        dataLab.append(int(values[1]))
    return dataMat,dataLab

df = pd.read_csv("C:/Users/user/Desktop/POC/ZbankPOC_Test_SZ2.csv",error_bad_lines=False)
dy=df[df.columns[0]]
dx=df[df.columns[1:]]
#x,dy=loadDataSet()
model=LogisticRegression()
model.fit(dx,dy)
print("the predict values is\n",model.predict([[1,3,0,3,1]]))
print('Coefficient:\n',model.coef_)
print('Intercept:\n',model.intercept_)