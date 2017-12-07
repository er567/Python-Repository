#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zgc
# @Date:   2017-05-17 10:18:05
# @Last Modified by:   Marte
# @Last Modified time: 2017-10-30 15:11:56
import urllib2
import re 
import os
import random
import requests
my_headers = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']
header = {"User-Agent":random.choice(my_headers), 'Cookie': 'AspxAutoDetectCookieSupport=1'}
url = 'http://www.meizitu.com/a/qingchun.html'
request = urllib2.Request(url,None,header)
file = urllib2.urlopen(request)
html = file.read()
reg = r"<a target='_blank' href=\"http://www.meizitu.com/a/.....html"
imgre = re.compile(reg)
urllist = re.findall(imgre,html)
for url in urllist:
    url = url.split('"')[1]
    print url
    request = urllib2.Request(url,None,header)
    file = urllib2.urlopen(request)
    html = file.read()
    reg = r'<title>.*</title>'
    imgre = re.compile(reg)
    titlist = re.findall(imgre,html)
    title=titlist[0]
    atitle=title[title.find('>')+1:title.find(' ')]
    # http://mm.chinasareview.com/wp-content/uploads/2017a/04/18/01.jpg
    reg = r'http://mm.chinasareview.com/wp-content/uploads/...../../../...jpg'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"}    
    dir=atitle+'/'
    if not os.path.isdir(dir):
        os.makedirs(dir)
    a=1
    for imgurl in imglist:
        img_url = requests.get(imgurl, headers=headers)
        print(img_url)
        f = open(dir+str(a)+'.jpg', 'wb')
        f.write(img_url.content)
        f.close()
        a+=1
