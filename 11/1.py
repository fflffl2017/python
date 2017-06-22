#!/usr/bin/env python
# -*- coding: utf-8 -*-
def ad(x, y):
    x = list(x)
    y = list(y)
    print x, y
    return map(lambda x, y: (x + y, int(x) + int(y)), x, y)


if __name__ == '__main__':
    x = tuple(input('pls enter yr num:'))
    y = tuple(input('pls enter your num:'))
    print ad(x, y)
