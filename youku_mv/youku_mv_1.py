# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.12
    @FileName：   youku_mv.py
    @CreateTime:  2017/3/21 8:32
    @Description: 
"""

import urllib2
from bs4 import BeautifulSoup


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
    html=getPage(url)

    soup=BeautifulSoup(html,'lxml')
    for s in soup.find_all('div',class_="p-thumb"):
        for i in s.find_all('a'):
            href = i.attrs["href"]
            title = i.attrs["title"]
        free = s.find_all('span', class_="vip-free")
        if len(free)==1:
            if_vip = r'会员免费'
        else:
            if_vip = r'免费'
        print "http:%s  %s  %s"%(href, title, if_vip)

    num = num + 1
