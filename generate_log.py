# -*- coding: utf-8 -*-
import random

#µã»÷ 1
#²¥·Å 2
#µãÔÞ 3
#ÊÕ²Ø 4
#¸¶·Ñ¹Û¿´ 5
#Õ¾Íâ·ÖÏí 6
#ÆÀÂÛ 7
def produce():
    final = ""
    file_object = open('./thefile.txt', 'w')
    albet_Num = ["a","b","c","d","e","f","g","h","1","2","3","4","5","6","7","A","B","C","D","E","O"]
    user_list = ["one","two","three","four","five"]
    num_array = ["1","2","3","4","5","6","7","8","9","0"]
    log_type_array = ["1","2","3","4","5","6","7"]
    topic_array = ["air purify","water purify","steam","filter"]
    for num in range(0,2000):
        cookie = "".join(random.sample(albet_Num, 10))
        uid = "".join(random.sample(user_list, 1)) #zhang san, li si, wangwu. registerd user id
        user_agent = "Safari"
        ip = "192.168.12.123"
        video_id = "".join(random.sample(num_array, 7))
        topic = "".join(random.sample(topic_array, 1))
        order_id = "0"
        log_type = "".join(random.sample(log_type_array, 1))

        final = final + (cookie + "&" + uid + "&" + user_agent + "&" + ip + "&" + video_id + "&" + topic + "&" + order_id + "&" + log_type + "\r\n")


    file_object.write(final)

    file_object.close()

def read_file():
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

    for k,v in click_action.items():
        print(k,len(v),v)

def read_file_cate():
    cate_list = {}
    file = open("./thefile.txt")
    for line in file.readlines():
        line = line.strip()
        ls = line.split("&")
        if ls[5] not in cate_list:
            cate_list[ls[5]]=[]
        cate_list[ls[5]].append(ls[4])
    file_object = open('./cat.log', 'w')
    for k,v in cate_list.items():
        line = k + "\t" + "&&".join(v) + "\r\n"
        file_object.write(line)
    file_object.close()
produce()
#read_file()
read_file_cate()
