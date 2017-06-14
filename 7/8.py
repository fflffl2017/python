#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    string=raw_input('>enter your string:')
    nstring=''
    for i in range(len(string)):
        if 65<=ord(string[i])<=77:
            nstring+=chr(ord(string[i])+13)
        elif 78<=ord(string[i])<=90:
            nstring+=chr(65+(90-ord(string[i])))
        elif 97<=ord(string[i])<=109:
            nstring+=chr(ord(string[i])+13)
        elif 110<=ord(string[i])<=122:
            nstring+=chr(97+(122-ord(string[i])))
        else:
            nstring+=string[i]
    print nstring

