#!/usr/bin/env python
# -*- coding: utf-8 -*-
def zhuanhuan(a):
    return (a-32)*(float(5)/float(9))

if __name__ == '__main__':
    a=float(raw_input('输入你的温度：'))
    print zhuanhuan(a)
