#!/usr/bin/env python
# -*- coding: utf8 -*-
import shelve
db=[]

def creatfile():
    a=raw_input('Pls enter your filename:')
    db.append(a)
    q=False
    while not q:
        b=raw_input('Pls enter your note:')
        if b!='q':
            db.append(b)
        else:
            q=True
    print db

def watchfile():
    f=shelve.open(db[0],'r')
    print f

def editfile():
    dd=[]
    q=False
    while not q:
        a=raw_input('Pls enter your edit note:')
        if a!='q':
            dd.append(a)
        else:
            q=True
    f=shelve.open(db[0],'c')
    f['data']=dd
    f.close()

def savefile():
    f=shelve.open(db[0],'c')
    f['data']=db[1:]
    f.close()

def quit():
    exit()


if __name__ == '__main__':
    while True:
        promt="""
        (C)reatfile
        (W)atchfile
        (E)ditfile
        (S)avefile
        (Q)uit
        """
        menu=raw_input(promt).lower()
        if menu not in 'cwesq':
            print 'wrong choice'
            continue
        if menu=='c':creatfile()
        if menu=='w':watchfile()
        if menu=='e':editfile()
        if menu=='s':savefile()
        if menu=='q':quit()
