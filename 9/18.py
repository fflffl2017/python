#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gzip
f_in=open('18.eg','r')
f_out=gzip.open('18.eg.gz','wb')
f_out.writelines(f_in)
f_in.close()
f_out.close()


