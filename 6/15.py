#!/usr/bin/env python
# -*- coding: utf-8 -*-
def findchr(a,b):
    for i in range(len(a)):
        if a[i]==b:
            return i+1
    return 'NO'
def rfindchr(a,b):
    for i in range(len(a)):
        if a[-(i+1)]==b:
            return len(a)-i
    return 'NO'


if __name__ == '__main__':
    a=raw_input('>输入你的长字符串：')
    b=raw_input('>输入你要查找的字符：')
    print findchr(a,b)
    print rfindchr(a,b)
