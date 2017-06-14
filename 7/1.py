#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s={'name':'Li','age':'20','sex':'boy'}
    values=s.values()
    values.sort()
    print values
    for value in values:
        for key in s.keys():
            if s[key]==value:
                print value,key

