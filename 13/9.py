#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Item(object):
    def __init__(self):
        self.book = 'php'
        self.food = 'python'


class Cart(Item):
    def __init__(self, n, m):
        super(Cart, self).__init__()
        self.num = {}
        self.num[self.book] = n
        self.num[self.food] = m

    def display(self):
        return self.num


class User(object):
    def __init__(self, s):
        self.s = s
        self.c = {}
        for i in range(s):
            self.m = int(raw_input('Enter your num of food:'))
            self.n = int(raw_input('Enter your num of book:'))
            q = Cart(self.n, self.m)
            self.c[i] = q.display()

    def show(self):
        for i in range(self.s):
            print self.c[i]


if __name__ == '__main__':
    c = User(2)
    d = User(1)
    a = raw_input('Enter your users:')
    if a == 'c':
        c.show()
    elif a == 'd':
        d.show()
