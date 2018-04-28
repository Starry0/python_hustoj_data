#-*- coding:utf-8 -*-

'''
@auther: Starry
@file: prodData.py
@time: 2018/1/17 15:47
'''

import random
import os

DATASIZE = 10

PLATFORM = "win"

def lin():
    for i in range(DATASIZE):
        with open('./data/test' + str(i) + '.in', 'w', encoding='utf-8') as f:
            T = random.randint(1, 100)
            f.write(str(T) + '\n')
            for j in range(T):
                N = random.randint(1, 10 ** 1000)
                f.write(str(N) + '\n')
        with open('./data/test' + str(i) + '.out', 'w', encoding='utf-8') as f:
            pass
        os.system('g++ -std=c++11 main.cpp -o main')
        # os.system('./main < data\\test' + str(i) + '.in >> data\\test' + str(i) + '.out')
        os.system('./main < data/test%s.in > data/test%s.out'%(i,i))
        print('第%s组数据已经生成' % i)
def win():
    for i in range(DATASIZE):
        print(i)
        with open('./data/test' + str(i) + '.in', 'w', encoding='utf-8') as f:
            a = random.randint(1,10**10000)
            b = random.randint(1,10**10000)
            f.write(str(a)+' '+str(b)+'\n')
            print(a+b)
            with open('./data/test' + str(i) + '.out', 'w', encoding='utf-8') as f1:
                f1.write(str(a*b))
        # os.system('g++ -std=c++11 main.cpp -o main')
        # os.system('main < data\\test' + str(i) + '.in >> data\\test' + str(i) + '.out')
        print('第%s组数据已经生成' % i)
if PLATFORM == "win":
    win()






