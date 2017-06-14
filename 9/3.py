#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    name=sys.argv[1]
    f=open(name,'r+')
    i=0
    while f.readline():
        i+=1
    print i
