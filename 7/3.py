#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import base64
import string

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
        else:
            print 'You already logged in at:',db[name1]
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



def showmenu():
    aaa="""
    (U)ser Login
    (D)elete User
    (L)ist user
    (Q)uit
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
            if choice not in 'uqdl':
                print 'invaild option,try again'
            else:
                chosen=True
        if choice=='q':done=True
        if choice=='u':user()
        if choice=='d':deluser()
        if choice=='l':listuser()

if __name__ == '__main__':
    showmenu()
