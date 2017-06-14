#!/usr/bin/env python
# -*- coding: utf-8 -*-
num_str=raw_input('Enter a number:')
num_num=int(num_str)
fac_list=range(1,num_num+1)
print "BEFORE:",fac_list
a=[i for i in range(1,num_num+1) if num_num%i!=0]
print "AFTER:",a
