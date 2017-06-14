#!/usr/bin/env python
# -*- coding: utf-8 -*-
def haha(a):
    c=0
    b=0
    for i in a:
        for k in range(len(i)):
            if i[k] in 'aeiou':
                c+=1
            else:
                b+=1
    return c,b

if __name__ == '__main__':
    a=raw_input('>').split(' ')
    print haha(a)
    print len(a)
