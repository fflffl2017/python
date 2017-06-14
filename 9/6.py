#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a=sys.argv[1]
    b=sys.argv[2]
    f=open(a,'r+')
    g=open(b,'r+')
    aa=f.readlines()
    bb=g.readlines()
    c=min(len(aa),len(bb))
    i=0
    n=0
    while i<c:
        if aa[i]==bb[i]:
            i+=1
        else:
            d=min(len(aa[i]),len(bb[i]))
            while n<=d:
                if aa[i][n]==bb[i][n]:
                    n+=1
                else:
                    print i+1,n+1
                    exit()
