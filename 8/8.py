#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    b=[1,1]
    i=3
    if a==1 or a==2:
        return 1
    else:
        while i<=a:
            b.append(b[i-2]+b[i-3])
            i+=1
        return b[-1]

if __name__ == '__main__':
    while True:
        a=int(raw_input('>'))
        print haha(a)
