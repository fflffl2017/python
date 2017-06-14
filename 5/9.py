#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a=float(raw_input('输入钱财总额：'))
    b=float(raw_input('输入每月消费：'))
    print'月份        消费金额        剩余金额'
    print'0           0               %.2f' % a
    m=0
    while a>b:
        a-=b
        m+=1
        print'%d           %.2f           %.2f' % (m,b,a)
    m+=1
    print'%d           %.2f            %.2f' % (m,a,0)

