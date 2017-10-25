# -*- coding:utf-8 -*-

__author__ = 'nacker'

import urllib
import urllib2

url = "http://www.baidu.com/s"
headers = {"User-Agent" : "Mozilla"}

keyword = raw_input("请输入需要查询的关键字")


wd = {"wd" : keyword}

# 通过urllib.urlencode() 参数是一个dict类型

wd = urllib.urlencode(wd)

# 拼接完整的url
fullUrl = url + "?" + wd

# 构造请求对象
request = urllib2.Request(fullUrl, headers = headers)

response = urllib2.urlopen(request)

print response.read()
