#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    name=sys.argv[1]
    i=0
    f=open(name,'r+')
    while i<=25:
        print f.readline()
        i+=1
        if i==25:
            a=raw_input('按任意键继续：')
            if a=='q':
                exit()
            else:
                i=0

