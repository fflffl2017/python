#!/usr/bin/env python
# -*- coding: utf-8 -*-
max2=lambda x,y:x if x>y else y
min2=lambda x,y:x if x<y else y

def my_max(*n):
    a=n[0]
    for i in n:
        a=max2(a,i)
    return a

def my_min(*n):
    a=n[0]
    for i in n:
        if i<a:
            a=i
    return a

if __name__=='__main__':
    print max2(1,2),min2(1,2),my_max(4,5,6,7),my_min(4,5,6,7)