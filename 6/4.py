#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    for i in range(len(a)):
        if i==0:
            print a[i+1]
        elif i==len(a)-1:
            print a[i]
        else:
            print a[i-1],a[i+1]


if __name__ == '__main__':
    a=raw_input('>')
    haha(a)
