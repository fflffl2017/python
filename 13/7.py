#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Queue(object):
    def __init__(self, data):
        self.data = data

    def enqueue(self, m):
        return self.data.append(m)

    def dequeue(self):
        s = self.data[0]
        self.data = self.data[1:]
        print self.data
        return s


if __name__ == '__main__':
    m = [1, 2, 3]
    q = Queue(m)
    q.enqueue(4)
    print q.dequeue()
    print q.dequeue()
