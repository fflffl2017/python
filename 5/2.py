#!/usr/bin/env python
# -*- coding: utf-8 -*-
def run(a):
    if a%4==0:
        if a%100!=0:
            return '是闰年'
        else:
            return '不是闰年'
    else:
        return '不是闰年'


if __name__ == '__main__':
    a=int(raw_input('输入你的年份：'))
    print run(a)
