#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)


if __name__ == '__main__':
    p = Point(12, 0)
    print p.show()
