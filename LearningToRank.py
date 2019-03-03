# -*- coding: utf-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder

def loadDataSet():
    path = "D:\\BaiduNetdiskDownload\\recommand\\users.feature_selection.data"
    data = np.loadtxt(path,dtype = int, delimiter='&&')
    
    x_train = data[:,:-1]
    y_train = data[:,-1]
    return x_train,y_train

if __name__ == "__main__":
    num_tree = 10
    x_train_full,y_train_ful = loadDataSet()
    x_train,x_test,y_train,y_test = train_test_split(x_train_full,y_train_ful,test_size=0.5)
    
    x_train_gbdt,x_train_lr,y_train_gbdt,y_train_lr = train_test_split(x_train,y_train,test_size=0.5)
    gbdt = GradientBoostingClassifier(n_estimators=num_tree)
    one_hot = OneHotEncoder()
    lr = LogisticRegression()
    gbdt.fit(x_train_gbdt,y_train_gbdt)
    
    x_leaf_index = gbdt.apply(x_train_gbdt)[:,:,0]
    x_lr_leaf_index = gbdt.apply(x_train_lr)[:,:,0]
    
    #print(x_leaf_index.shape)
    #print(x_lr_leaf_index.shape)
    one_hot.fit(x_leaf_index)
    x_lr_one_hot = one_hot.transform(x_lr_leaf_index)
    #print(x_lr_one_hot)
    
    lr.fit(x_lr_one_hot,y_train_lr)
    
    y_predict = lr.predict_proba(one_hot.transform(gbdt.apply(x_test[0:1,:])[:,:,0]))
    
    #print(y_predict)
    mapPro = {}
    for i in range(1,113):
        mapPro[i] = y_predict[0][i-1]
    
    mapPro = sorted(mapPro.items(),key=lambda x:x[1],reverse=True)
    #print(mapPro)
    print("---------------------------------------------")
    print(mapPro[0:10])
    print("=============================================")
    print(mapPro[0:10][0][0])  # the category which has the most probality
    print(mapPro[0:10][0][1])  #the propality of the category
    
    
