#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a,b,c):
    for i in range(a,b+1,c):
        print i

if __name__ == '__main__':
    a=int(raw_input('>from:'))
    b=int(raw_input('>to:'))
    c=int(raw_input('increment:'))
    haha(a,b,c)
