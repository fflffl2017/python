#!/usr/bin/env python
# -*- coding: utf-8 -*-
def ip2int(a):
    for i in range(len(a)):
        a[i]=hex(int(a[i]))[2:]
        if len(a[i])==1:
            a[i]='0'+a[i]
    print int(a[0]+a[1]+a[2]+a[3],16)

if __name__ == '__main__':
    a=raw_input('>输入你的ip地址：').split('.')
    ip2int(a)

