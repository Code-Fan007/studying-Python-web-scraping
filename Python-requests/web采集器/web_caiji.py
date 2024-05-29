#!usr/bin/env python3.11
# -*- coding: utf-8 -*-
import requests
#if这行的意思是：在代码运行的时候，会有一个内置变量，__name__，
#将其命名为__main__，一般用来自己写模块的时候调试用的，这样导入这个模块，就不会执行下面的语句
if __name__=="_main__":
    #UA伪装：将对应的user-agent信息封装到headers(字典)中
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    url ='https://www.sogou.com/web'
    #处理url携带的参数：封装到字典中
    kw=input("enter a word:")
    param={
        'query':kw
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response=requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    fileName =kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')