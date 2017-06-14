#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    b=[]
    c=[]
    b=a.keys()
    c=a.values()
    d=dict(zip(c,b))
    print d

if __name__ == '__main__':
    a={'name':'li','age':'19','sex':'boy'}
    haha(a)
