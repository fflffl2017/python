#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self,hr=0,min=0,turple=(),dict={},str=''):
        'Time60 constructor - take hours and minutes'
        self.hr=hr
        self.min=min

    def __str__(self):
        'Time60 - string representation'
        if self.min>10:
            return '%d:%d' % (self.hr,self.min)
        else:
            return '%d:%s' % (self.hr,'0'+str(self.min))

    __repr__=__str__

    def __add__(self, other):
        'Time60 - overloading the addition operator'
        return self.__class__(self.hr+other.hr,self.min+other.min)
    def __iadd__(self, other):
        'Time60 - overloading in-place addition'
        self.hr += other.hr
        self.min += other.min
        return self

if __name__ == '__main__':
    t=Time60(12,5)
    print t
