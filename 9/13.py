#!/usr/bin/env python
# -*- coding : utf-8 -*-

import sys
import pickle
db=[]
if __name__ == '__main__':
    a=raw_input('Pls enter your first filename:')
    b=raw_input('Pls enter your second filename:')
    f=open(a,'r+')
    for i in f.readlines():
        print i
        db.append(i)
    print db
    f.close()
    f=open(b,'w+')
    pickle.dump(db,f)
    f.close()
    f=open(b,'r')
    pickle.load(f)
    print f
