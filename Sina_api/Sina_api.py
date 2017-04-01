from weibo import APIClient  
import webbrowser#python内置的包
import json

APP_KEY = '2998674744'  
APP_SECRET = 'e91f3899e27e6533e2988589af9c3414'  
CALLBACK_URL = 'http://f.dataguru.cn/'  
  
#利用官方微博SDK  
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)  
#得到授权页面的url，利用webbrowser打开这个url  
url = client.get_authorize_url()  
print url  
webbrowser.open_new(url)  

code = 'e678582018e51dc837a449f8a15294e4'
#获取token
r = client.request_access_token(code)  
access_token = r.access_token # 新浪返回的token，类似abc123xyz456  
expires_in = r.expires_in  # token过期的UNIX时间
uid = r.uid
# 设置得到的access_token  
client.set_access_token(access_token, expires_in)

users = client.friendships.friends.get(uid=uid, count=100)['users']
length = len(users)
list01 = []
for i in range(0,length):
    list01.append(users[i]['location'].encode('GBK','ignore'))
    list01[i] = list01[i].split()[0]

list02 = set(list01)
dict01 = {}
for item in list02:
    dict01.update({item:list01.count(item)})
#输出了部分信息
for i in range(0,length):
    print u'昵称：'+users[i]['screen_name'].encode('GBK','ignore')
    print u'简介：'+users[i]['description'].encode('GBK','ignore')
    print u'位置：'+users[i]['location'].encode('GBK','ignore')
print ""
print u'位置统计：'+json.dumps(dict01,encoding='utf-8',ensure_ascii=False)
