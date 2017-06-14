#!usr/bin/env python
# -*- coding : utf-8 -*-
import sys

if __name__ == '__main__':
    a=sys.argv
    if len(a)==4:
        b=int(a[1])
        c=a[2]
        d=int(a[3])
        if c=='+':print b+d
        if c=='-':print b-d
        if c=='*':print b*d
        if c=='/':print b/d
