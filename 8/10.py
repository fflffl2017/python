#!/usr/bin/env python
# -*- coding: utf-8 -*-
db=[]

if __name__ == '__main__':
    i=1
    b=0
    while i<=5:
        a=raw_input('Enter your name(Firstname,Lastname):')
        if a=='q':
            break
        a=a.split(',')
        if len(a)!=2:
            b+=1
            print 'Please enter correct name.'
            continue
        else:
            db.append(a)
        i+=1
    print db,b


