#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Message(object):
    def __init__(self, name, tag, str=''):
        self.name = name
        self.massage = str
        self.tag = tag

    def say(self):
        return str(self.name) + ' in ' + str(self.tag) + ' said: ' + str(self.massage)


class Room(object):
    def __init__(self, tag):
        self.tag = tag


class User(Room):
    def __init__(self, name='nobody', tag=0):
        self.tag = tag
        super(User, self).__init__(self.tag)
        self.name = name
        self.message = raw_input('Enter your message')
        self.m = Message(self.name, self.tag, self.message)

    def say(self):
        return self.m.say()


if __name__ == '__main__':
    a = User()
    print a.say()
