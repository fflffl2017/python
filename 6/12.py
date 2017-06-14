#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    b=''
    for i in range(len(a)):
        if 97<=ord(a[i])<=122:
            b+=chr(ord(a[i])-32)
        elif 65<=ord(a[i])<=90:
            b+=chr(ord(a[i])+32)
        else:
            b+=a[i]
    print b

if __name__ == '__main__':
    a=raw_input('输入你的字符串吧，大兄弟：')
    haha(a)
