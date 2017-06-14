#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    string=raw_input('>')
    a=''
    for i in range(len(string)):
        if 68<=ord(string[i])<=90:
            a+=chr(ord(string[i])-13)
        elif 65<=ord(string[i])<=67:
            a+=chr(90-(13-(ord(string[i])-65)))
        elif 110<=ord(string[i])<=122:
            a+=chr(ord(string[i])-13)
        elif 97<=ord(string[i])<=109:
            a+=chr(122-(13-(ord(string[i])-97)))
        else:
            a+=string[i]
    print a
