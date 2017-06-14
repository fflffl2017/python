#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    b=''
    for i in range(len(a)):
        if a[i]==' ':
            pass
        else:
            b+=a[i]
    return b

if __name__ == '__main__':
    a=raw_input('输入字符串：')
    print haha(a)
