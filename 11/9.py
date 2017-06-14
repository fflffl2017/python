#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
if __name__=='__main__':
    files=filter(lambda x:x and x[0]!='.',os.listdir('/'))
    print files