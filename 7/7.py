#!/usr/bin/env python
# -*- coding: utf-8 -*-
def tr(srcstr,dststr,string):
    if srcstr in string:
        a=string.split(srcstr)
        if len(a)==2:
            if a[0]=='':
                b=dststr+a[1]
                print b
            elif a[-1]=='':
                b=a[0]+dststr
                print b
            else:
                b=a[0]+dststr+a[1]
                print b

if __name__ == '__main__':
    srcstr=raw_input('>srcstr:')
    dststr=raw_input('>dststr:')
    string=raw_input('>string:')
    tr(srcstr,dststr,string)
