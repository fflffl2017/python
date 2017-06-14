#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import tarfile
import os

def uncompress(path,filename):
    endlist=['tbz','tar.gz','tar','tar.bz2','tgz','bz2','gz']
    filesplit=filename.split('.',1)
    if filename.endswith('.zip'):
        f=zipfile.ZipFile(filename,'r')
        f.extractall(path)
    elif filesplit[1] in endlist:
        f=tarfile.open(filename,'r')
        f.extractall(path)

def decompress(target,*filenames):
    if not os.path.exists(target):
        os.mkdir(target)
    uncompress(target,filenames[0])
    for name in filenames[1:]:
        diname=os.path.splitext(os.path.basename(name))[0]
        diname=target+'/'+diname
        os.mkdir(diname)
        uncompress(diname,name)

if __name__=='__main__':
    os.chdir('/home/coffee/')
    decompress('fang','18.eg.gz','20.zip','22.tar','22.tar.gz','22.tar.gz.bz2')