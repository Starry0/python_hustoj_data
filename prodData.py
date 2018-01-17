#-*- coding:utf-8 -*-

'''
@auther: Starry
@file: prodData.py
@time: 2018/1/17 15:47
'''

import random
import os

DATASIZE = 10


for i in range(DATASIZE):
    with open('./data/test'+str(i)+'.in','w',encoding='utf-8') as f:
        N = random.randint(1, 100)
        W = random.randint(1, 10000)
        f.write(str(N)+' '+str(W)+'\n')
        for j in range(N):
            a = random.randint(1,10000)
            b = random.randint(1,10000)
            f.write(str(a) + ' ' + str(b)+'\n')
    with open('./data/test'+str(i)+'.out','w',encoding='utf-8') as f:
        pass
    os.system('g++ -std=c++11 main.cpp -o main')
    os.system('main < data\\test'+str(i)+'.in >> data\\test'+str(i)+'.out')




