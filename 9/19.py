#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
f_in=gzip.open('18.eg.gz','rb')
f_out=open('19.eg','wb')
content=f_in.read()
f_out.write(content)
f_out.close
f_in.close()
