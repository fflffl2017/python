#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Mix(object):
    def __init__(self, data):
        self.data = data

    def shift(self):
        self.data = self.data[1:]
        return self.data

    def unshift(self, m):
        self.data = m + self.data
        return self.data

    def push(self, m):
        self.data.append(m)
        return self.data

    def popp(self):
        if 'pop' in dir(self.data):
            return self.data.pop()


if __name__ == '__main__':
    s = [1, 2, 3, 4]
    mix = Mix(s)
    print mix.shift()
    str = eval('[' + '9' + ']')
    print mix.unshift(str)
    print mix.push(5)
    print mix.popp()
    print mix.popp()
