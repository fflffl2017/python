#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
if __name__ == '__main__':
    a=raw_input('输入你的数字组合：')
    b=a.split()
    print sorted(b)
    c=[]
    for i in b:
        d=int(i)
        c.append(d)
    print sorted(c)

