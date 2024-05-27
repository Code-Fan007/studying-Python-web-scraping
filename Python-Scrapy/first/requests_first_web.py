#!usr/bin/env python3
# -*- coding: utf-8 -*-
#需求：爬取搜狗首页的页面数据
import requests
if __name__ == '__main__':
    #step1: 指定url
    url = 'http://www.sogou.com/'
    #step2: 发起请求
    #git方法会返回一个响应对象；
    response = requests.get(url=url)
    #step3: 打印响应数据（在响应对象里面）
    page_text = response.text
    print(page_text)
    #step4: 保存响应数据到文件(持久化存储)
    with open('sogou_homepage.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('保存成功！')
