#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a=raw_input('输入你要查看的模块：')
    m=__import__(a)
    print dir(m)
