#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import pickle


class Database(object):
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
        self.flag = False

    def update(self, name, passwd):
        self.name = name
        self.passwd = passwd
        self.time = str(time.time())
        tm = self.name + ':' + self.passwd + ':' + self.time
        self.tmp = file('db.txt', 'ab')
        self.db = pickle.dump(tm, self.tmp, True)
        self.tmp.close()

    def check(self):
        self.tmp = file('db.txt', 'rb')
        a = []
        while True:
            try:
                self.db = pickle.load(self.tmp)
                a.append(self.db)
            except:
                self.tmp.close()
                break
        if len(a) > 1:
            for i in range(len(a)):
                if not isinstance(a[i], list):
                    print a[i]
                    if self.name == a[i].split(':')[0]:
                        if self.passwd == a[i].split(':')[1]:
                            print "login success"
                            print a[i].split(':')[2]
                            Database.__del__(self, a, i)
                else:
                    for k in range(len(a[i])):
                        if self.name == a[i][k].split(':')[0]:
                            if self.passwd == a[i][k].split(':')[1]:
                                print 'login success'
                                print a[i][k].split(':')[2]
                                return Database.__del__(self, a[i], k)
        else:
            print len(a)
            a = a[0]
            while isinstance(a, list):
                a = a[0]
                print a
                for i in range(len(a)):
                    if self.name == a[i].split(':')[0]:
                        if self.passwd == a[i].split(':')[1]:
                            print "login success"
                            if self.name == 'admin':
                                self.flag = True
                                print "Welcome my admin"
                                return Database.__del__(self, a, i)

    def __del__(self, a, i):
        print a, i
        self.time = time.time()
        a[i] = self.name + ':' + self.passwd + ':' + str(self.time)
        self.tmp = file('db.txt', 'wb')
        self.db = pickle.dump(a, self.tmp, True)
        self.tmp.close()
        return a[i]

    def admin(self):
        if self.flag == True:
            n = raw_input("Do you want to see all the acount?(yes/no)")
            if n == 'yes':
                self.tmp = file('db.txt', 'rb')
                a = []
                while True:
                    try:
                        self.db = pickle.load(self.tmp)
                        a.append(self.db)
                    except:
                        break
                print a
            else:
                print "ok,maybe next time"


if __name__ == '__main__':
    name = raw_input('Enter your name:')
    passwd = raw_input('Enter your passwd:')
    m = Database(name, passwd)
    # m.update('guest', 'guest')
    m.check()
    m.admin()
