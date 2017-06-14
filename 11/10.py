#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
def clfile(filename):
    n=raw_input('''
    c:creat a new file
    o:overwrite this file
    ''')
    if n=='c':
        f=open(filename,'r')
        a=filename+'1'
        l=open(a,'w')
        m=map(lambda x:x.strip(),f)
        for i in m:
            l.write(i)
            l.write(os.linesep)
        l.close()
    if n=='o':
        f=open(filename,'r')
        m=map(lambda x:x.strip(),f)
        f.close()
        f=open(filename,'w')
        for i in m:
            f.write(i)
            f.write(os.linesep)
        f.close()

if __name__=='__main__':
    clfile('10.eg')