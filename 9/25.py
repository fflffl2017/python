#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile,tarfile

def movefile(compress1,compress2,filename):
    type1=compress1.split('.',1)
    type2=compress2.split('.',1)
    if type1[1]=='zip':
        z=zipfile.ZipFile(compress1,'r')
        if filename in z.namelist():
            z.extract(filename)
            z.close()
        else:
            print 'no such file.'
            z.close()
            return
    else:
        mode='r:bz2'if type1[1][-2:]=='tar.bz2'else'r:gz'
        z=tarfile.open(compress1,mode)
        if filename not in f.getnames():
            print 'no such file'
            return
        else:
            z.extract(filename)
        z.close()

    if type2[1]=='zip':
        z=zipfile.ZipFile(compress2,'a')
        if filename in z.namelist():
            print 'file already exist.'
            return
        else:
            z.write(filename)
            print 'add success'
        z.close()

    else:
        filelist=[]
        z=tarfile.open(compress2,'r')
        for i in z.getnames():
            filelist.append(i)
        if filename in filelist:
            print 'file aleardy exist'
            return
        else:
            mode='w:gz'if type2[1][-2:]=='gz'else'w:bz2'
            z.close()
            z=tarfile.open(compress2,mode)
            filelist.append(filename)
            for k in filelist:
                z.add(k)
            z.close()
            print 'add success'

if __name__=='__main__':
    movefile('20.zip','22.tar.gz','20_1.eg')
