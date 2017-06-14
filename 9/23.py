#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tarfile

f=tarfile.open('22.tar','r')
f.extractall()
f.close()
