#!/usr/bin/env python
# -*- coding: utf-8 -*-
def printf(n,m):
    for i in range(len(m)):
        if m[i]=='%':
            if m[i+1]=='d':
                return m[:i],int(n),m[i+2:]

if __name__=='__main__':
    for i in printf('33','I have %d books'):
        print i,


