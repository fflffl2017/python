#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a=sys.argv[1]
    f=open(a,'r')
    db=[]
    dd=[]
    for i in f.readlines():
        db.append(i)
    f.close()
    for i in db:
        print len(i)
        if len(i)<=80:
            dd.append(i)
        else:
            b=len(i)/80
            for k in range(b):
                u=k*80
                dd.append(i[u:u+80])
            dd.append(i[(b*80):])
            print len(i[b*80:])
    f=open(a,'a+')
    for j in dd:
        m=j+'\n'
        f.write(m)
    f.close()
