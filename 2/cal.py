#!/usr/bin/env python
# -*- coding: utf-8 -*-
def add(y,z):
    return y+z

def mul(y,z):
    return y*z

if __name__ == '__main__':
    while 1:
        print'(a)两数相加求和'
        print'(b两数相乘求积)'
        print'(x)退出'
        y=int(raw_input('输入你的第一个数字:'))
        z=int(raw_input('输入你的第二个数字:'))
        x=raw_input('输入你的选项：')
        if x=='a':
            print add(y,z)
        elif x=='b':
            print mul(y,z)
        elif x=='x':
            exit()

