#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    while True:
        a=set(raw_input('输入集合A：'))
        b=set(raw_input('输入集合B：'))
        c=raw_input('输入运算符号(或q)：')
        print a,b
        if c=='in':print a in b
        if c=='not in':print a not in b
        if c=='<':print a<b
        if c=='>':print a>b
        if c=='!=':print a!=b
        if c=='==':print a==b
        if c=='q':exit()

