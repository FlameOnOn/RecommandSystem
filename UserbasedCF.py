# -*- coding: utf-8 -*-

import math

class UCF:
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
    
    def UserSimilarity(self):
        #建立用户-用户的共现矩阵
        C = dict() #用户-用户共现矩阵
        N = dict() #用户购买过多少商品
        
        
        #对同一商品有过行为的用户集合
        self.item_users = dict()
        for user, items in self.train.items():
            for i in items.keys():
                self.item_users.setdefault(i,[])
                #if i not in self.item_users:
                 #   self.item_users[i] = set()
                self.item_users[i].append(user)
        
        for i, users in self.item_users.items():
            for u in users:
                N.setdefault(u,0)
                N[u]+=1
                for j in users:
                    if u == j:
                        continue
                    C.setdefault(u,{})
                    C[u].setdefault(j,0)
                    C[u][j] += 1
        
        self.W = dict()
        for u, related_users in C.items():
            self.W.setdefault(u,{})
            for v, cuv in related_users.items():
                self.W[u][v] = cuv / math.sqrt(N[u] * N[v])
        
        return self.W
        
    #给user推荐
    def recommand(self,user,K=3,N=10):
        rank = dict() 
        action_item = self.train[user].keys() #用户user有过行为的物品
        for v, wuv in sorted(self.W[user].items(),key=lambda x:x[1],reverse = True)[0:K]:
            for i, rvi in self.train[v].items():
                if i in action_item:
                    continue
                rank.setdefault(i,0)
                rank[i] += wuv * rvi
        
        return dict(sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N])

    
if __name__ == "__main__":
    path = "D:\\BaiduNetdiskDownload\\recommand\\ml-100k\\ml-100k\\u.data"
    cf = UCF(path,path)
    cf.UserSimilarity()
    print(cf.recommand('3'))
        
             
                        
                
            
            
        
