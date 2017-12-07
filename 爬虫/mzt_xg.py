#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os
url_list, title_list = [], []
res = requests.get("http://www.mzitu.com/xinggan/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
pins = soup.select('#pins li span a')
for i, pin in enumerate(pins):
    z = 1
    res = requests.get(pin['href'])
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    pageSize = int(soup.select(".dots + a span")[0].text)
    url = pin['href']
    # file_name = 'images/'+pin.string
    if not os.path.exists(pin.string):
        os.makedirs(pin.string)
        os.chdir(pin.string)
    while z < pageSize:
        loadUrl = url + '/' + str(z)
        res = requests.get(loadUrl)
        soup = BeautifulSoup(res.text, 'html.parser')
        src = soup.select('.main-image img')[0]['src']
        headers = {"Referer": url}
        img = requests.get(src, headers=headers)
        print(os.getcwd())
        with open('{i}.jpg'.format(i=z), 'wb') as code:
            code.write(img.content)
        z = z + 1
        if z == pageSize:
            os.chdir(os.path.pardir)