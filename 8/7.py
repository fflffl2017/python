#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    b=1
    for i in range(1,a+1):
        b*=i
    return b

if __name__ == '__main__':
    a=int(raw_input('>'))
    print haha(a)
