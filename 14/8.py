#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def usage():
    print 'At least 2 argument (inc1. cmd name).'
    print 'usage: args.py arg1 arg2 [arg3...]'
    sys.exit(1)


argc = len(sys.argv)
if argc < 3:
    usage()
print 'number of args enterd:', argc
print 'arg(inc1. cmd name) were:', sys.argv
