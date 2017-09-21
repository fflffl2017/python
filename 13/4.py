#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import *


class Line(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __repr__(self):
        return ((self.x1, self.y1), (self.x2, self.y2))

    def length(self):
        le = sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        return le

    def slope(self):
        s = ((self.x1 - self.x2) / (self.y1 - self.y2))
        return s


if __name__ == '__main__':
    l = Line(12, 12, 13, 13)
    print l.__repr__()
    print l.length()
    print l.slope()
