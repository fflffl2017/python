#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    filename=sys.argv[1]
    num=int(sys.argv[2])
    f=open(filename,'r+')
    i=0
    while i<=num:
        print f.readline()
        i+=1

