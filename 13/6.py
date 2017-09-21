#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Stack(object):
    def __init__(self, s):
        self.data = s

    def push(self, m):
        self.data.append(m)
        return self.data

    def isempty(self):
        if self.data == []:
            return False
        else:
            return True

    def peek(self):
        return self.data[-1]

    def has_pop(self):
        # if 'pop' in dir(self.data):
        #    return self.data.pop()
        # else:
        #   self.p = self.data[-1]
        #    self.data = self.data[:-1]
        #   return self.p
        if hasattr(self.data, 'pop'):
            return '1'
        else:
            return '0'


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5]
    n = []
    stack = Stack(s)
    print stack.push(6)
    print stack.peek()
    print stack.has_pop()
    # print stack.has_pop()
    nn = Stack(n)
    print nn.isempty()
