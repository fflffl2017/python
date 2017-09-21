#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import *
import os
class Shell(object):
    def more(self,filename):
        return call(('more',filename))
    def ll(self,path):
        f=os.popen('ls -al')
        self.data=f.readlines()
        return self.data
if __name__ == '__main__':
    while True:
        shell=Shell()
        s=raw_input('>').split(' ')
        if s[0]=='more':
            print shell.more(s[1])
        if s[0]=='ll':
            for i in shell.ll(os.getcwd()):
                print i