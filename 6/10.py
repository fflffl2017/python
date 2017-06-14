#!/usr/bin/env python
# -*- coding: utf-8 -*-
def abc(a):
    x=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    y=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    z='hundred'
    if len(a)==4:
        print 'one thousand'
    elif len(a)==1:
        a=int(a)
        print x[a-1]
    elif len(a)==2:
        if int(a)<20:
            a=int(a)
            print x[a-1]
        else:
            print y[int(a[0])-1],'-',x[int(a[1])-1]
    elif len(a)==3:
        print x[int(a[0])-1],z,'-',y[int(a[1])-1],'-',x[int(a[2])-1]


if __name__ == '__main__':
    a=raw_input('Enter your number(1-1000):')
    abc(a)
