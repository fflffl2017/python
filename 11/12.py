#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
mult=lambda x,y:x*y

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*factorial(n-1))


if __name__=='__main__':
    n=raw_input('pls enter your num:')
    a1=time.time()
    print reduce(mult,range(1,int(n)+1))
    a2=time.time()
    print reduce(lambda x,y:x*y,range(1,int(n)+1))
    a3=time.time()
    print factorial(int(n))
    a4=time.time()
    print a2-a1,a3-a2,a4-a3