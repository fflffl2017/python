#!/usr/bin/env python
# -*- coding: utf-8 -*-
db={}

if __name__ == '__main__':
    while True:
        name=raw_input('输入你的员工名字：')
        number=raw_input('输入你的员工编号：')
        db[name]=number
        for i in sorted(db.values()):
            for key in db.keys():
                if db[key]==i:
                    print i,key
