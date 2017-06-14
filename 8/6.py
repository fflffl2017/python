#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    b=[]
    for i in range(1,a):
        if a%i==0:
            b.append(i)
    c=0
    for k in b:
        c+=k
    if c==a:
        return a

if __name__ == '__main__':
    #a=int(raw_input('>'))
    for a in range(1,1001):
        if 1<=haha(a)<=1000:
            print haha(a)
