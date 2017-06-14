#!/usr/bin/env python
# -*- coding: utf-8 -*-
def add(a,b):
    return a+b
def miu(a,b):
    return a-b
def mul(a,b):
    return a*b
def chu(a,b):
    return a/b
def yua(a,b):
    return a%b
def fan(a,b):
    return a**b


if __name__ == '__main__':
    a=raw_input('输入你的算式：').split()
    a[0]=int(a[0])
    a[2]=int(a[2])
    print a
    if a[1]=='+':
        print add(a[0],a[2])
    if a[1]=='-':
        print miu(a[0],a[2])
    if a[1]=='*':
        print mul(a[0],a[2])
    if a[1]=='/':
        print chu(a[0],a[2])
    if a[1]=='%':
        print yua(a[0],a[2])
    if a[1]=='**':
        print fan(a[0],a[2])
