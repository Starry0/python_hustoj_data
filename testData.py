#-*- coding:utf-8 -*-

'''
@auther: Starry
@file: testData.py
@time: 2018/1/17 15:46
'''

import os

DATASIZE = 10

os.system('g++ -std=c++11 test.cpp -o test')
PLATFORM = "win"


def win():
    WA = False
    for i in range(DATASIZE):
        os.system('./test < data/test%s.in > te.out' % i)
        flag = os.system('fc data\\test' + str(i) + '.out te.out > nul')
        if flag != 0:
            print('Wrong answer on test' + str(i) + '.in!!!')
            WA = True

    if not WA:
        print("Accepted!!!")
def lin():
    WA = False
    for i in range(DATASIZE):
        os.system('./test < data/test%s.in > te.out' % i)
        flag = os.system("diff data/test%s.out te.out"%i)
        if flag != 0:
            print('Wrong answer on test' + str(i) + '.in!!!')
            WA = True

    if not WA:
        print("Accepted!!!")

if PLATFORM == "win":
    win()