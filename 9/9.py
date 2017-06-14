#!/usr/bin/env python
# -*- coding: utf-8 -*-
#有__doc__属性的意思就是py里有被“”“包裹起来的文字
import os
import sys

lis=[]
def fin(allname):
    for i in os.listdir(allname):
        if os.path.isdir(allname+'/'+i):
            fin(allname+'/'+i)
        else:
            lis.append(allname+'/'+i)

fin('/usr/lib/python2.7')
f1=open('hasdoc.txt','a+')
f2=open('nohasdoc.txt','a+')
strn=''
hasDOC=False
for i in lis:
    print i
    f=open(i)
    for eachline in f.readlines():
        if (not hasDOC)and eachline.startswith('"""'):
            hasDOC=True
        elif hasDOC and eachline.startswith('"""'):
            hasDOC=False
            strn+=eachline
            break
        if hasDOC:
            strn+=eachline
        else:
            break
    if strn!='':
        f1.write('filename:'+i+'\n')
        f1.write("__doc__"+"\n")
        f1.write(strn+'\n')
    else:
        f2.write('文件名:'+i+'\n')
    strn=''
    f.close()
f1.close()
f2.close()
