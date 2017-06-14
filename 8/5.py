#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    c=[]
    d=[]
    b=1
    for i in range(2,a):
        if a%i==0:
            c.append(i)
    print c
    for k in c:
        for l in range(2,k):
            if k%l==0:
                b=0
        if b==1:
            d.append(k)
    print d



if __name__ == '__main__':
    a=int(raw_input('>'))
    haha(a)
