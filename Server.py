# -*- coding: utf-8 -*-
import socket

HOST,PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print("Serving HTTP on port ..." , PORT)


def Processing(request):
    uid="1"
    return uid

class Rec:
    def process(self, request):
        uid = "1"
        return self.rec(uid)
   
    def rec(self, uid):
        rec = "123"
        return rec

r = Rec()

def gp(uid):
    click_action = {}   # key: uid, value: video_id
    file = open("./thefile.txt")
    for line in file.readlines():
        line = line.strip()
        ls = line.split("&")
        if ls[7] != "1":
            continue
        if ls[1] not in click_action.keys():
            click_action[ls[1]] = []
        click_action[ls[1]].append(ls[4])

    if uid in click_action.keys():
        return "&&".join(click_action[uid])

comment_log = {} #key:uid, value:video_ids
def log_process(request):
    print(request)
    request = request.strip()
    ls = request.split("&")
    if ls[1] not in comment_log.keys():
        comment_log[ls[1]]=[]
    comment_log[ls[1]].append(ls[4])

    for k,v in comment_log.items():
        print(k, v)

    return "got it"

#pre process
file = open("./cat.log")
cate_list = {}
for line in file.readlines():
    line = line.strip()
    ls = line.split("\t")
    if ls[0] not in cate_list.keys():
        cate_list[ls[0]] = []
    lss = ls[1].split("&&")
    for v in lss:
        cate_list[ls[0]].append(v)

def log_process_one(request,tag):
    #request can be number of word
    #word: return the matched items, tag == 1
    #number: return the tong leimu items, tag == 2
    if tag == 1:
        if request in cate_list.keys():
            return "&&".join(cate_list[request])
        else:
            return "wrong requst, doesn't contain the item"
    elif tag == 2:
        for k,v in cate_list.items():
            if request in v:
                return "&&".join(v)
        return "wrong number , no items in the same category"
    else:
        print(tag)
        return "wrong reqeust"


while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    #print("***")
    #print(Processing(request))
    #print(r.process(request))
    #print("***")
    #http_response=gp(request)
    #http_response = log_process(request)
    paras,tag = request.strip().split("&&")
    http_response = log_process_one(paras,int(tag.strip()))
    print(http_response)
    client_connection.sendall(http_response)
    client_connection.close()
