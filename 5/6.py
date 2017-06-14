#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a,b):
    if a%b==0:
        return 'yes'
    else:
        return 'no'

if __name__ == '__main__':
    a=int(raw_input('输入你的第一个数：'))
    b=int(raw_input('输入你的第二个数：'))
    print haha(a,b)
