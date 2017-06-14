#!/usr/bin/env python
#-*- coding:utf-8 -*-
def hb(x,y):
    return map(lambda x,y:(x,y),x,y)

if __name__=='__main__':
    x=[1,2,3]
    y=['abc','def','hig']
    print hb(x,y)
    print zip(x,y)