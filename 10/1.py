#!/usr/bin/env python
#-*- coding:utf-8 -*-
def opfile(name):
    try:
        f=open(name,'r')
    except IOError:
        return None
    return f

if __name__=='__main__':
    f=opfile('2333')
    print type(f)
