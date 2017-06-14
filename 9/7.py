#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    f=open('/etc/services','r')
    i=0
    while i<20:
        print f.readline()
        i+=1
