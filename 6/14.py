#!/usr/bin/env python
# -*- coding: utf-8 -*-
def int2ip(a):
    hexs=hex(int(a))[2:]
    while len(hexs)<8:
        hexs='0'+hexs
    ip1=int(hexs[0]+hexs[1],16)
    ip2=int(hexs[2]+hexs[3],16)
    ip3=int(hexs[4]+hexs[5],16)
    ip4=int(hexs[6]+hexs[7],16)

    print '%d.%d.%d.%d' % (ip1,ip2,ip3,ip4)

if __name__ == '__main__':
    a=raw_input('>输入你的整数吧，少年：')
    int2ip(a)
