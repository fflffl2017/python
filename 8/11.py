#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a,b):
    for i in range(a,b+1):
        print i,hex(i)[2:],oct(i)[1:],bin(i)[2:],chr(i)

if __name__ == '__main__':
    a=int(raw_input('Enter your start number:'))
    b=int(raw_input('Enter your last number:'))
    haha(a,b)
