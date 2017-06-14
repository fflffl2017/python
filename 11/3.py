#!/usr/bin/env python
# -*- coding: utf-8 -*-
def tex(a,b,tx=0.3):
    return a*b*tx

if __name__=='__main__':
    print tex(1,2,0.2)
    print tex(1,2)