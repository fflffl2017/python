#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find(a,b):
    ch=chr(a)
    f=open(b,'r')
    num=0
    for i in f:
        num+=i.count(ch)
    return num


if __name__ == '__main__':
    a=int(raw_input('enter your number(0-255):'))
    b=raw_input('enter your filename:')
    print find(a,b)
