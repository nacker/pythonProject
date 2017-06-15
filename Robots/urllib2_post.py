# -*- coding:utf-8 -*-

__author__ = 'nacker'

import urllib
import urllib2

# 通过抓包的方式获取的url，并不是浏览器上显示的url
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null"

# 完整的headers
headers = {
    # "Host": "fanyi.youdao.com",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

# 用户接口输入
key = raw_input("请输入需要翻译的文字:")

# 发送到web服务器的表单数据
formdata = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt" : "1497431564487",
    "sign" : "b3bc1a34df9d89f148978ad8ed09e252",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTON",
    "typoResult": "true",
}

# 经过urlencode转码
data = urllib.urlencode(formdata)

# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = urllib2.Request(url, data=data, headers=headers)

# print urllib2.urlopen(request).read()

dict = urllib2.urlopen(request).read()

print (dict)


