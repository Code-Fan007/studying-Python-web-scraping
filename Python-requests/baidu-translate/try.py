#!usr/bin/env python3.11
# -*- coding: utf-8 -*-
import requests
import json
if __name__ == '__main__':
# 破解百度翻译；1、post请求2、响应数据是一组json数据
    # 1.指定Url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    #3. post请求参数处理（同get请求一致）
    word=input("请输入要翻译的单词：")
    date={
        'kw': 'dog'
        }
    # 4.请求发送
    response=requests.post(url=post_url, data={'kw': 'dog'})
    # 5.获取响应数据:json()方法返回的是obi（如果响应数据是json才能用）
    dic_obj=response.json()
    # 持久化储存
    fileNames= word +'.json'
    fp=open('fileNames','w',encoding='utf-8')
    json.dump(dic_obj,fp,ensure_ascii=False)
    print("保存成功")
