#!/usr/bin/env python
#-*- coding:utf-8 -*-
def run(a):
    if a%4==0:
        if a%100!=0:
            return True
        else:
            pass
    else:
        pass

if __name__=='__main__':
    y=[1990.1992,1994,1996,1998,2000]
    print filter(run,y)
