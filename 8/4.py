#!/usr/bin/env python
# -*- coding: utf-8 -*-
def getfactors(a):
    b=[]
    for i in range(1,a+1):
        if a%i==0:
            b.append(i)
    print b

if __name__ == '__main__':
    a=int(raw_input('>'))
    getfactors(a)
