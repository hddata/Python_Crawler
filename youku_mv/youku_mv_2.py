# !/usr/bin/python

# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.12
    @CreateTime:  2017/3/6 15:15
    @Description: 优酷电影
"""
import urllib2
import re
def getPage(url):
    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        # 构建请求的request
        request = urllib2.Request(url, headers=headers)
        # 利用urlopen获取页面代码
        response = urllib2.urlopen(request)
        # 将页面转化为UTF-8编码
        pageCode = response.read().decode('utf-8')
        return pageCode

    except urllib2.URLError, e:
        if hasattr(e, "reason"):
            print u"连接失败,错误原因", e.reason
            return None
num = 1
while(31-num):
    url = "http://list.youku.com/category/show/c_96_s_1_d_1_p_%s.html"%num
    html = getPage(url)
    lin = r'<div class="p-thumb">(?:.|\n)*?<a href="(.+?)" title="(.+?)" target="_blank"'
    link = re.compile(lin)
    link_list = re.findall(link,html)

    for i in link_list:
        print "%s  http:%s"%(i[1],i[0])
    num = num +1
