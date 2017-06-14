#!/usr/bin/env python
# -*- coding: utf-8 -*-
def subchr(a,b,c):
    d=''
    for i in range(len(a)):
        if a[i]!=b:
            d+=a[i]
        else:
            d+=c
    return d

if __name__ == '__main__':
    a=raw_input('>输入你要替换的字符串：')
    b=raw_input('>输入你要被替换的字符：')
    c=raw_input('>输入替换它的字符：')
    print subchr(a,b,c)
