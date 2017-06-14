#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    b=''
    for i in range(len(a)-1):
        b+=a[-i-2]
    print a+b

if __name__ == '__main__':
    a=raw_input('输入字符串：')
    haha(a)
