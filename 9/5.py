#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    argv=[]
    for i in range(len(sys.argv)):
        if i!=0:
            argv.append(sys.argv[i])
    print argv
    for i in argv:
        f=open(i,'r+')
        print f.readlines()

