#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a,b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            return '两字符串不相等'
    return '两字符串相等'

if __name__ == '__main__':
    a=raw_input('输入第一个字符串：')
    b=raw_input('输入第二个字符串：')
    if len(a)!=len(b):
        print '两字符串不相等'
    else:
        print haha(a,b)
