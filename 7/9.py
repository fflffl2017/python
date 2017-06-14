#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

n=random.randrange(1,10,1)
m=random.randrange(1,10,1)
s=set()
v=set()
for i in range(n):
    a=random.randint(0,9)
    s.add(a)
for l in range(m):
    b=random.randint(0,9)
    v.add(b)
print v,s
x= (v|s)
y= (v&s)
xx=[]
yy=[]
aa=raw_input('>enter a|b answer:')
bb=raw_input('>enter a&b answer:')
for nn in range(len(aa)):
    xx.append(int(aa[nn]))
for mm in range(len(bb)):
    yy.append(int(bb[mm]))
xx=set(xx)
yy=set(yy)
if (xx&x)==x:
    print 'OK,|'
if (yy&y)==y:
    print 'OK,&'
cc=raw_input('输入个子集吧：')
gg=[]
for ee in range(len(cc)):
    gg.append(int(cc[ee]))
gg=set(gg)
print gg
if gg<=v:
    print 'ok'

