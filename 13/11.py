#!/usr/bin/env python
# -*- coding: utf-8 -*-
class G(object):
    def __init__(self, name, num, date, price, count):
        self.name = name
        self.num = num
        self.date = date
        self.price = price
        self.count = count

    def show(self):
        return str(self.name) + ' : ' + \
               str(self.num) + ' : ' + str(self.date) + ' : ' + str(self.price) + ' : ' + str(self.count)


class Database(object):
    def __init__(self):
        self.db = {}

    def new(self, name, num, date, price, count):
        self.db[num] = G(name, num, date, price, count).show()

    def all_count(self, num):
        return int(self.db[num].split(' : ')[3]) * int(self.db[num].split(' : ')[4]) * 0.3

    def show(self):
        a = []
        for i in self.db:
            a.append(self.db[i])
        return a


if __name__ == '__main__':
    d = Database()
    d.new('a', 1, 2017 - 5 - 3, 12, 100)
    d.new('b', 2, 2017 - 9 - 8, 22, 100)
    print  d.all_count(1)
    print  d.show()
