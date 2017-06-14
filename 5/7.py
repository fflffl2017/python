#!/usr/bin/env python
# -*- coding: utf-8 -*-
def dd(a,b):
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            n=i
    return n

def ee(a,b):
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            n=i
    return a*b/n

if __name__ == '__main__':
    a=int(raw_input('输入第一个数：'))
    b=int(raw_input('输入第二个数：'))
    print dd(a,b)
    print ee(a,b)
