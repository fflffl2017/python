#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


class Time(object):
    def __init__(self, mytime=datetime.datetime.now()):
        self.time = mytime

    def update(self, mytime=datetime.datetime.now()):
        self.time = mytime
        return self.display(self.choice)

    def display(self, choice='default'):
        self.choice = choice
        if self.choice == 'MDY':
            return self.time.strftime('%m/%d/%y')
        elif self.choice == 'MDYY':
            return self.time.strftime('%m/%d/%Y')
        elif self.choice == 'DMY':
            return self.time.strftime('%d/%m/%y')
        elif self.choice == 'DMYY':
            return self.time.strftime('%d/%m/%Y')
        elif self.choice == 'MODYY':
            return self.time.strftime('%a/%d/%y')
        elif self.choice == 'default':
            return self.time


if __name__ == '__main__':
    time1 = raw_input('Enter your time:(year,month,day)').split(',')
    choice = raw_input('Enter your choice:')
    mytime = datetime.date(int(time1[0]), int(time1[1]), int(time1[2]))
    t = Time(mytime)
    print t.display(choice)
    print t.update()
