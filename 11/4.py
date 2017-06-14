#!/usr/bin/env python
# -*- coding: utf-8 -*-
def mt(n):
    return n/60,n%60

if __name__=='__main__':
    x=mt(77)
    print x[1]
    print '%d hour %d min' % (x[0],x[1])