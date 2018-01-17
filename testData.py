#-*- coding:utf-8 -*-

'''
@auther: Starry
@file: testData.py
@time: 2018/1/17 15:46
'''

import os

DATASIZE = 10

os.system('g++ test.cpp -o test')
WA = False
for i in range(DATASIZE):
    os.system('test < data\\test'+str(i)+'.in > te.out')
    flag = os.system('fc data\\test'+str(i)+'.out te.out > nul')
    if flag != 0:
        print('Wrong answer on test'+str(i)+'.in!!!')
        WA = True

if not WA:
    print("Accepted!!!")
