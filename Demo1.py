# coding=utf-8
from numpy import *
import pandas as pd

def subSstr(str,substr):
    try:
        return str.find(substr)
    except Exception as e:
        return -1

def insetSubstr(str,inValue,inserIndex):
    try:
        iv=str.index(inValue)
        print(iv)
        if iv > 0:
            return iv
        else:
            str.insert(inserIndex,inValue)
            print(str)
            return "inser sucess"
    except Exception as e:
        print(e)
        return -1

if __name__ == '__main__':
    print(insetSubstr([1,2,3],4,3))
    colors=["red","green","blue"]
    for i,color in enumerate(colors):
        if color=='green':
            print("the %s is exits",color,i)
   # df = pd.DataFrame({'total_bill': [16.99, 20.11, 10.74]},'tip':[1.01,1.31,2.12],'sex':['Female','Male','Male']})
    df = pd.DataFrame({'total_bill': [16.99, 10.34, 23.68, 23.68, 24.59],
                       'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
                       'sex': ['Female', 'Male', 'Male', 'Male', 'Female']})
    list=['total_bill', 'ti7p', 'sex']
    #print(df[list].head(5))
    #print(df[df['sex']=='Male'].head(5))
    is_Male=df['sex']=='Male'
    print(df[df['sex']=='Male'])
    print(map(lambda x,y:x+y,range(1,10)))