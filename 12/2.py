#!/usr/bin/env python
# -*- coding: utf-8 -*-
def importAS(n):
    return __import__(n)


if __name__ == '__main__':
    n = 'os'
    n = importAS(n)
    print n.path
