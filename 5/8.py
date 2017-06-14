#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

if __name__ == '__main__':
    N=random.randint(2,100)
    randlist=random.sample(range(0,2**31-1),N)
    print randlist
    randlist.sort()
    print randlist
