#!/usr/bin/env python
# -*- codig: utf-8 -*-
from login import *
import time
import datetime


class Change(Database):
    def __init__(self, name, passwd):
        super(Change, self).__init__(name, passwd)

    def cpasswd(self):
        print Database.check(self)
        if int(str(datetime.date.fromtimestamp(time.time() - \
                                                       float(Database.check(self).split(':')[2]))) \
                       .split('-')[0]) < 1971:
            print 'you should change your password'
            password = raw_input('Enter your new password:')
            Database.update(self, self.name, password)


if __name__ == '__main__':
    c = Change('admin', 'abc')
    print c.cpasswd()
