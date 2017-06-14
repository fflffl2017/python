#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmath
def safe_sqrt(n):
    try:
        return cmath.sqrt(n)
    except ValueError:
        n=abs(n)
        
