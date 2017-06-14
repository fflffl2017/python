#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import base64
import string
import shelve
import pickle
db={}

def newuser(name):
    j=string.ascii_lowercase+string.digits
    while True:
        for k in name:
            if k not in j:
                print 'wrong username,try another'
                return 0
        if db.has_key(name):
            prompt='name taken,try another:'
            continue
        else:
            break
    pwd=raw_input('passwd:')
    pwd=base64.b64encode(pwd)
    db[name]=pwd
    a=datetime.datetime.now()
    name1=name+'1'
    db[name1]=a
    f=open('user.txt','a+')
    a=str(a)
    r=name+':'+pwd+':'+a+';'+'\n'
    r=str(r)
    f.write(r)
    f.close

def olduser(name):
    pwd=raw_input('passwd:')
    pwd=base64.b64encode(pwd)
    passwd=db.get(name)
    name1=name+'1'
    dat=datetime.datetime.now()
    dd=db.get(name1)
    if passwd==pwd:
        if (dat-dd).seconds>=240:
            print 'welcome back',name
            if name=='admin':
                print 'You are administrator'
                for i in db.keys():
                    print i,db[i]
        else:
            print 'You already logged in at:',db[name1]
            for i in db.keys():
                print i,db[i]
    else:
        print 'login incorrect'

def user():
    name=raw_input('login:')
    if name not in db.keys():
        a=raw_input('new user?[Y/N]:').lower()
        if a=='y':
            newuser(name)
        else:
            print 'no user'
            return 0
    else:
        olduser(name)

def deluser():
    name=raw_input('Enter the user you want to delete:')
    name1=name+'1'
    if name in db.keys():
        del db[name]
        del db[name1]
        print db
    else:
        print 'no user in my db'


def listuser():
    for key in db.keys():
        if key[-1]!='1':
            print key,db[key]

def saveuser():
    sh=shelve.open('user1.txt','c')
    sh['data']=db
    sh.close()
    sh=shelve.open('user1.txt','r')
    print sh['data']

def saveuser1():
    sh=open('user2.txt','w')
    pickle.dump(db,sh)
    sh.close()

    sh=open('user2.txt','r')
    f=pickle.load(sh)
    print f
def showmenu():
    aaa="""
    (U)ser Login
    (D)elete User
    (L)ist user
    (Q)uit
    (S)helve
    (P)ickle
    Enter choice """

    done=False

    while not done:
        chosen=False
        while not chosen:
            try:
                choice=raw_input(aaa).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice='q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'uqdlsp':
                print 'invaild option,try again'
            else:
                chosen=True
        if choice=='q':done=True
        if choice=='u':user()
        if choice=='d':deluser()
        if choice=='l':listuser()
        if choice=='s':saveuser()
        if choice=='p':saveuser1()

if __name__ == '__main__':
    showmenu()
