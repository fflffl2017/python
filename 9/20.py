#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile

def creat(zipname,filename1,filename2):
    f=zipfile.ZipFile(zipname,'w')
    f.write(filename1)
    f.write(filename2)
    f.close

def add(zipname,filename):
    f=zipfile.ZipFile(zipname,'a')
    f.write(filename)
    f.close

def extract(zipname,filename):
    f=zipfile.ZipFile(zipname,'r')
    f.extract(filename)
    f.close()

if __name__ == '__main__':
    while True:
        a=raw_input('pls input your choice(caeq):')
        if a=='q':exit()
        if a=='c':creat('20.zip','20_1.eg','20_2.eg')
        if a=='a':add('20.zip','20_3.eg')
        if a=='e':extract('20.zip','20_3.eg')
