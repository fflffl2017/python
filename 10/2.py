#!/usr/bin/env python
# -*- coding:utf-8 -*-
def safe_input():
    try:
        a=raw_input('pls etr yr wd')
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None
    print a
    return 'OK'
if __name__=='__main__':
    f=safe_input()
    print type(f)