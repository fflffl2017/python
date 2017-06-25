#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import os

f = Popen(('ls', '-al'), stdout=PIPE, shell=True).stdout
p = Popen('sort', stdin=PIPE, stdout=PIPE, shell=True)
data = f.readlines()
f.close()
for d in data:
    print d.split('\n')[0]
    p.stdin.write(d)
p.stdin.close()
print '-' * 20
print p.stdout.read()
p.stdout.close()
