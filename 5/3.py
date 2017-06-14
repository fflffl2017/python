#!/usr/bin/env python
# -*- coding: utf-8 -*-
def mc(a):
    a*=100
    a=int(a)
    b=a/25
    i=a%25
    c=i/10
    i%=10
    d=i/5
    i%=5
    return (b,c,d,i)

if __name__ == '__main__':
    a=float(raw_input('输入你的金额(小于1):'))
    b=mc(a)
    print "%d个25美分,%d个10美分,%d个5美分,%d个1美分" % (b[0],b[1],b[2],b[3])
