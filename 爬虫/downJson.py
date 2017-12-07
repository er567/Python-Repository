#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-10-31 15:47:01
# @Last Modified by:   Marte
# @Last Modified time: 2017-10-31 17:03:35
import urllib2
import os
import random
my_headers = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']
header = {"User-Agent":random.choice(my_headers), 'Cookie': 'AspxAutoDetectCookieSupport=1'}
url = 'https://www.panc.cc/js/getmovie.php?'
z = 1
if not os.path.exists('json/'):
  os.makedirs('json/')
  os.chdir('json/')
while z < 100:
  loadUrl = '{url}{z}'.format(url=url,z=z)
  request = urllib2.Request(loadUrl,None,header)
  response = urllib2.urlopen(request)
  #将带有结果集的response读取出来，并赋值给content
  content = response.read().decode('unicode_escape').encode('utf-8')   
  # json_result = json.loads(content)       
  print content
  with open('{i}.json'.format(i=z), 'wb') as code:
    code.write(content) 
    z += 1      