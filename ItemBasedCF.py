# -*- coding: utf-8 -*-
import math

class ItemBasedCF:
    #初始化对象
    def __init__(self,train_file,test_file):
        self.train_file = train_file # 训练数据
        self.test_file = test_file  #测试数据
        self.readData()    #读取数据
    
    def readData(self):
        #读取文件，生成用户-物品的评分表和测试集
        self.train = dict() #训练集
        #按行读取文件
        for line in open(self.train_file):
            #获得用户，物品，评分，丢弃时间戳数据
            user,item,score,_=line.strip().split("\t")
            #用户-物品评分矩阵
            self.train.setdefault(user,{})
            self.train[user][item] = int(score)
        
        self.test = dict() #测试集
        for line in open(self.test_file):
            user,item,score,_ = line.strip().split("\t")
            self.test.setdefault(user,{})
            self.test[user][item] = int(score)
    
    def ItemSimilarity(self):
        #建立物品-物品的共现矩阵
        C = dict() #物品-物品共现矩阵
        N = dict() #物品被多少个不同用户购买
        #遍历训练数据，获得用户有过行为的物品
        for user, items in self.train.items():
            #遍历该用户每件物品项
            for i in items.keys():
                N.setdefault(i,0)
                N[i]+=1
                for j in items.keys():
                    if i == j:
                        continue
                    C.setdefault(i,{})
                    C[i].setdefault(j,0)
                    C[i][j]+=1
        
        #计算相似度矩阵
        #计算物品-物品相似度
        #遍历物品-物品的共现矩阵的所有项
        self.W = dict() #存放物品的相似度
        for i, related_items in C.items():
            self.W.setdefault(i,{})
            for j, cij in related_items.items():
                self.W[i][j] = cij/(math.sqrt(N[i] * N[j]))
        
        return self.W
    #给user推荐
    def recommand(self,user,K=3,N=10):
        rank = dict() #用户user对物品的偏好值
        action_item = self.train[user] #用户user产生过行为的物品以及其评分
        for item, score in action_item.items():
            #遍历与物品item最相似的前k个物品，获得这些物品及相似分数
            for j,wj in sorted(self.W[item].items(),key=lambda x:x[1],reverse=True)[0:K]:
                if j in action_item.keys():
                    continue
                #计算用户user对物品i的偏好值，初始化该值为0
                rank.setdefault(j,0)
                rank[j] += score * wj
        #按照评分值大小，为用户推荐结果取前N个物品
        return dict(sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N])
    
if __name__ == "__main__":
    path = "D:\\BaiduNetdiskDownload\\recommand\\ml-100k\\ml-100k\\u.data"
    cf = ItemBasedCF(path,path)
    cf.ItemSimilarity()
    print(cf.recommand('3'))
        
             
                        
                
            
            
        
