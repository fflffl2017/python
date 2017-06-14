#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    for i in (0,len(a)/2):
        if a[i]==a[-(i+1)]:
            pass
        else:
            return '没戏'
    return 'OK'

if __name__ == '__main__':
    a=raw_input('>')
    if len(a)%2==0:
        print '没戏'
    else:
        print haha(a)
