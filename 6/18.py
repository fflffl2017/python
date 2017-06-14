#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def haha(a):
    b=random.randint(0,2)
    c=['石头','剪刀','布']
    d=c[b]
    if a=='石头':
        if d=='石头':
            return '---'
        elif d=='剪刀':
            return 'Y'
        else:
            return 'N'
    if a=='剪刀':
        if d=='剪刀':
            return '---'
        elif d=='石头':
            return 'N'
        else:
            return 'Y'
    if a=='布':
        if d=='石头':
            return 'Y'
        elif d=='剪刀':
            return 'N'
        else:
            return '---'


if __name__ == '__main__':
    a=raw_input('输入你的选择：')
    print haha(a)
