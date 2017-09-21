#!/usr/bin/env python
# -*- coding: utf-8 -*-
class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return 'self.file'

    def write(self, line):
        self.file.write(line)

    def writelines(self):
        self.a = open('13.txt', 'r')
        self.data = self.a.readlines()
        self.a.close()
        self.a = open('13.txt', 'w')
        self.a.write(self.data.)  # zi ji gai ba

    def __getattr__(self, attr):
        return getattr(self.file, attr)


if __name__ == '__main__':
    f = CapOpen('13.txt', 'w')
    f.write('dadas\ndasdsad\ndasdsadsa\n')
    f.file.close()
    f = CapOpen('13.txt', 'r')
    t = f.file.readlines()
    for i in t:
        print i
    f.file.close()
    f = CapOpen('13.txt', 'r')
    f.writelines()
    f.file.close()
    f = CapOpen('13.txt', 'r')  # keng
    t = f.file.readlines()
    for i in t:
        print i
    f.file.close()
