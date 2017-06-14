#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isprime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

if __name__ == '__main__':
    a=int(raw_input('>'))
    if isprime(a):
        print 'Yes!'
    else:
        print 'No'
