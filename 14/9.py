#!/usr/bin/env python
# -*- coding: utf-8 -*-
x = -1


def foo(x):
    if x < 0:
        return False
    else:
        return True


foo.test = '''
if foo(x):
    print 'ok'
else:
    print 'wrong'
'''
if hasattr(foo, 'test'):
    print 'y'
    exec foo.test
else:
    print 'n'
