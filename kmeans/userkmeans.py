# -*- coding: utf-8 -*-


from sklearn.cluster import KMeans
import numpy as np
from sklearn import preprocessing
def loadDataSet():
    path = "D:\\BaiduNetdiskDownload\\recommand\\users.data"
    data = np.loadtxt(path,dtype = int, delimiter='&&')
    x_data = data[:,:-1]
    x_pre_data = preprocessing.MinMaxScaler().fit_transform(x_data)
    return x_data, x_pre_data

def kmeansC(oriDataSet,preDataSet):
    #for item in range(1,15):
        #print(item)
    #n_cluster_can = np.arange(2,20)
    #after elbow method, the best cluster number is 4
    #SSE_previous = 0
    #for cluster_can in n_cluster_can:
        #kmeans = KMeans(n_clusters=cluster_can, random_state=0).fit(dataSet)
        #y_predict = kmeans.fit_predict(dataSet)
        #print(kmeans.labels_)
        #print(metrics.calinski_harabaz_score(dataSet,y_predict))
        #SSE = kmeans.inertia_
        
        #print(cluster_can)
        #print(SSE_previous - SSE)
        #SSE_previous = SSE
    n_cluster_final = 4 
    kmeans = KMeans(n_clusters=n_cluster_final, random_state=0).fit(preDataSet)
    labes = kmeans.labels_
    #print(labes)
    newDataSet = np.insert(oriDataSet,len(oriDataSet[0]),values=labes,axis=1)
    #print(newDataSet[0:3,:])
    return newDataSet
def getSubDataSet(newDataSet):
    dataSet0 = []
    dataSet1 = []
    dataSet2 = []
    dataSet3 = []
    for line in newDataSet:
        if line[64] == 0:
            dataSet0.append(line)
        elif line[64] == 1:
            dataSet1.append(line)
        elif line[64] == 2:
            dataSet2.append(line)
        elif line[64] == 3:
            dataSet3.append(line)
    dataSet0 = np.array(dataSet0)
    dataSet1 = np.array(dataSet1)
    dataSet2 = np.array(dataSet2)
    dataSet3 = np.array(dataSet3)
    
    file_object_0 = open('./user_data_0','w')
    createPartData(dataSet0,file_object_0)
    file_object_1 = open('./user_data_1','w')
    createPartData(dataSet1,file_object_1)
    file_object_2 = open('./user_data_2','w')
    createPartData(dataSet2,file_object_2)
    file_object_3 = open('./user_data_3','w')
    createPartData(dataSet3,file_object_3)
    
def createPartData(dataSet,file_object):
    entry = ""
    for line in dataSet:
        for item in line:
            entry += str(item) + "&&"
        entry = entry.strip('&&')
        entry += "\n"
    file_object.write(entry)
    file_object.close()
    
  
if __name__ == "__main__":
    oriDataSet,preDataSet = loadDataSet()
    #newDataSet is the dataset with the catagory got from k-means 
    newDataSet = kmeansC(oriDataSet,preDataSet)
    #dataSet1,dataSet2,dataSet3,dataSet4 = getSubDataSet(newDataSet)
    getSubDataSet(newDataSet)
