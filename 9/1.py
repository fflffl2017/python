#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

v=sys.argv[1]
f=open(v,'r+')
for eachline in f:
    for i in range(len(eachline)):
        if eachline[i]=='#':
            print eachline[0:i]
            break


