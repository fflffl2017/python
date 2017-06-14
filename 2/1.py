#!/usr/bin/env python
# -*- coding: utf-8 -*-

def abc(a,b):
    c=d=0
    for i in range(len(a)):
        c+=int(a[i])
        d+=int(b[i])
    c=float(c)/len(a)
    d=float(d)/len(b)
    return (c,d)
if __name__ == '__main__':
    a=[1,2,1,1,1]
    b=(6,7,8,9,10)
    print abc(a,b)

