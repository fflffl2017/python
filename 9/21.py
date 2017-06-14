#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile,time

if __name__ == '__main__':
    f=zipfile.ZipFile('20.zip','r')
    for i in f.infolist():
        precent=float(i.compress_size)/i.file_size *100
        print '20.eg'
        print precent,i.compress_size,i.file_size
        t=time.ctime(time.mktime(tuple(list(i.date_time)+[0,0,0])))
        print t

