# -*- coding: utf-8 -*-

import numpy as np
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
def loadDataSet():
    path = "D:\\BaiduNetdiskDownload\\recommand\\users.feature_selection.data"
    data = np.loadtxt(path,dtype = int, delimiter='&&')
    
    x_train = data[:,:-1]
    y_train = data[:,-1]
    print(x_train.shape)
    print(y_train.shape)
    return x_train, y_train

def featureSelect(train_data, test_data):
    svc = LinearSVC(C=0.01, penalty="l1",dual=False).fit(train_data,test_data)
    model = SelectFromModel(svc, prefit=True)
    x_train_new = model.transform(x_train)
    
    print(x_train_new.shape)


if __name__ == "__main__":
    x_train,y_train = loadDataSet()
    featureSelect(x_train,y_train)
