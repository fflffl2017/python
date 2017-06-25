#!/usr/bin/env python
# -*- coding:utf-8 -*-
def f(n):
    flist = [0, 1, 1]
    if 1 == n or 2 == n:
        return 1
    else:
        for i in range(2, n):
            flist.append(f(i) + flist[i - 1])
    return flist[n]


print f(6)
