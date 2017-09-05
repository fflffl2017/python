#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, os


def checkurl(url):
    regex = re.compile(
        r'^(?:http|ftp)?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9]{2,}\.?)|'
        r'localhost'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex.match(url):
        return True
    else:
        return False


def geturl():
    name = raw_input('pls enter the name of the website:')
    url = raw_input('pls enter your url:')
    if checkurl(url):
        pass
    else:
        print 'wrong url,pls try again'
    mark = raw_input('pls enter your mark:')
    folder = raw_input('pls enter your floder:')
    return (name, url, mark, folder)


def load(filename):
    f = open(filename, 'a+')
    bmlist = f.readlines()
    f.close()
    return bmlist


def save(bmlist, filename):
    f = open(filename, 'w+')
    for line in bmlist:
        if len(line):
            continue
        f.write(line)
    f.close()


def add(bmlist, name, url, mark, folder='default'):
    bookmark = ''
    bookmark = name + ';' + url + ';' + mark + ';' + folder + os.linesep
    if bookmark not in bmlist:
        bmlist.append(bookmark)


def modify(bmlist, index, name, url, mark, folder):
    bookmark = ''
    bookmark = name + ';' + url + ';' + mark + ';' + folder + os.linesep
    bmlist[index] = bookmark


def delbm(bmliist, index):
    bmlist.pop(idnex)


def findbk(bmlist, fname, furl):
    for i, item in enumerate(bmlist):
        (name, url, mark, folder) = item.split(';')
        if fname and furl:
            if (fname in name) and (furl in url):
                return i
        if fname and (fname in name):
            return i
        if furl and (furl in url):
            return i
        else:
            return -1


def output2html(bmlist):
    for i, item in enumerate(bmlist):
        (name, url, mark, folder) = item.split(';')
    os.mkdir(folder.strip())
    filename = name.strip() + '.html'
    f.open(filename, 'w+')
    fmt = '%d\t%s\t<a href=%s>%s</a>\t%s\t%s<br>'
    f.write('<html><head><title>bookmark</title></head><body>')
    content = fmt % (i + 1, name, r'http://' + url, url, mark, folder)
    f.write(content)
    f.write('</body></html>')
    f.close()
    os.rename(filename, folder.strip() + os.sep + filename)


bmlist = load('url.txt')
print bmlist
while True:
    print '0.quit'
    print '1.add a url bookmark'
    print '2.modify a url bookmark'
    print '3.delete a url bookmark'
    print '4.find a url bookmark'
    print '5.out url bookmark as html'
    print '\n'

    oo = int(raw_input('pls enter your operation num:'))
    if (0 == oo):
        save(bmlist, r'url.txt')
        break
    # elif(oo<0 or oo>5):
    #    print 'wrong number,try again'
    elif oo == 1:
        data = geturl()
        add(bmlist, *data)
        print bmlist
    elif 2 == oo:
        index = int(raw_input('bookmark index:'))
        data = geturl()
        modify(bmlist, index, *data)
        print bmlist
    elif 3 == oo:
        index = int(raw_input('bookmark index:'))
        delbm(bmlist, index)
        print bmlist
    elif 4 == oo:
        name = raw_input('url name:')
        url = raw_input('url address:')
        index = findbk(bmlist, name, url)
        if index == -1:
            print 'not found'
        else:
            print bmlist[index]
    elif 5 == oo:
        output2html(bmlist)
