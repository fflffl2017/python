#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这道题就把不是规定字符的字符先随机出来，然后在加上n个规定字符，然后用random.shuffle()方法把字符串打乱即可，我做的复杂了
import random
def randfile(a,b,c):
    db=[]
    dd=''
    for i in range(b):
        a=random.randint(0,c-1)
        if a not in db:
            db.append(a)
    print db
    for k in range(0,c):
        for m in db:
            print k
            if k==m:
                print m
                dd+=chr(a)
                print dd+'\n'
            else:
                q=False
                while not q:
                    bb=random.randint(0,255)
                    if bb!=a:
                        dd+=chr(bb)
                        q=True
    print dd



if __name__ == '__main__':
    a=int(raw_input('Pls enter your num:'))
    b=int(raw_input('Pls enter your times:'))
    c=int(raw_input('Pls enter your 额。。长度:'))
    randfile(a,b,c)
