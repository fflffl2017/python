#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from subprocess import call

a = os.system('ls -al')
b = call(('cat', '/etc/motd'))
