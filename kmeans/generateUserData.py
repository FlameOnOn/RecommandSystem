# -*- coding: utf-8 -*-

import numpy as np
def generateData():
    #feature: gendor, age, num_of_phones, location(one-hot), previous 6-month behaviour, total volumn consumed
    #total item consumed(short message), total balance consumed
    #lable:  from 1 to 112
    entry = ""
    file_object = open('./users.data','w')
    for user_id in range(1,20001):
        gendor = np.random.randint(0,2,1)
        num_of_phones = np.random.randint(1,4,1)
        location = np.random.randint(0,2,43)
        previous_short_message = np.random.randint(1,200,6)
        previous_volumn = np.random.randint(0,10000,6)
        previous_call_time = np.random.randint(0,10000,6)
        label = np.random.randint(1,113,1)
        entry += str(user_id)
        for item in gendor:
            entry += "&&" + str(item)
        #entry = str(user_id) + "&&" + gendor
        for item in num_of_phones:
            entry += "&&" + str(item)
        for item in location:
            entry += "&&" + str(item)
        for item in previous_short_message:
            entry += "&&" + str(item)
        for item in previous_volumn:
            entry += "&&" + str(item)
        for item in previous_call_time:
            entry += "&&" + str(item)
        for item in label:
            entry += "&&" + str(item)
        entry += "\n"
    file_object.write(entry)
    file_object.close()
    return  

if __name__ == "__main__":
    generateData()
