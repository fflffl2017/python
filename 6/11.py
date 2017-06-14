#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    a=int(a)
    b=a/60
    c=a%60
    print b,'hours and',c,'minutes'

if __name__ == '__main__':
    a=raw_input('Enter your minutes:')
    haha(a)
