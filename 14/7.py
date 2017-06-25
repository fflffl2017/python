#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    while 1:
        a = raw_input('enter your cmd:')
        if a == 'exit':
            break
        else:
            b = os.popen(a).readlines()
            for i in b:
                print i.split('\n')[0]
