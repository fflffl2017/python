#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

a = os.popen('ls')
f = a.read()
print f
print '-' * 50
b, c = os.popen2('sort')
b.write(f)
print '-' * 50
print c.read()
a.close()
b.close()
c.close()
