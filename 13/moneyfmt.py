#! /usr/bin/env python
# -*- coding: utf-8 -*-
class MoneyFmt(object):
    def __init__(self, dollar=0,flag=True):
        self.dollar = dollar
        self.flag=flag

    def __nonzero__(self):
        if not self.dollar == 0:
            return True
        else:
            return False

    def __repr__(self):
        return self.dollar

    def dollarize(self):
        a = ''
        b = ''
        s = str(self.dollar).split('.')[0]
        for i in range(len(s)):
            if i % 3 != 0:
                a += s[-i - 1]
            else:
                a += ','
                a += s[-i - 1]
        for i in range(len(a)):
            b += a[-i - 1]
        if b[-1] == ',':
            b = b[:-1]
        z = str(self.dollar).split('.')[1]
        if self.flag:
            return b + '.' + z
        else:
            return '<'+b[1:]+'.'+z+'>'

    def upadte(self, dollar=0):
        self.dollar = dollar
        new = self.dollarize()
        return new


if __name__ == '__main__':
    dollars = float(raw_input('Count your money:'))
    mon = MoneyFmt(dollars,False)
    print mon.__doc__
    print mon.dollarize()
    print mon.__nonzero__()
    print mon.__repr__()
    while True:
        dollar = float(raw_input('Count your money again:'))
        print mon.upadte(dollar)
