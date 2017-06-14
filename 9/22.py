#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tarfile
f=tarfile.open('22.tar','w')
f.add('22.eg')
f.close

f=tarfile.open('22.tar.gz','w:gz')
f.add('22.eg')
f.close()

f=tarfile.open('22.tar.gz.bz2','w|bz2')
f.add('22.eg')
f.close()


