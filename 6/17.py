#!/usr/bin/env python
# -*- coding: utf-8 -*-
def atoc(a):
    b=[]
    c=[]
    b=a.split('+')
    c=a.split('-')
    if len(b)==2:
        return complex(int(b[0]),int(b[1]))
    if len(c)==2:
        return complex(int(c[0]),-int(c[1]))


if __name__ == '__main__':
    a=raw_input('>输入你的复数字符串：').split('j')
    print atoc(a[0])
