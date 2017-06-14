#!/usr/bin/env python
# -*- coding: utf-8 -*-
def gra(a):
    if 90<=a<=100:
        return 'a'
    if 80<=a<90:
        return 'b'
    if 70<=a<80:
        return 'c'
    if 60<=a<70:
        return 'd'
    if a<60:
        return 'fuck'

if __name__ == '__main__':
    a=int(raw_input('请输入你的成绩:'))
    print gra(a)
