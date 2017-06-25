#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def my_exit_func():
    print 'your are wrong'


sys.exitfunc = my_exit_func

if __name__ == '__main__':
    print 1
    print 2
    print 3
    exit()
