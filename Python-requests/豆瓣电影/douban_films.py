#!usr/bin/env python3.11
# -*- coding: utf-8 -*-
import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
       'type': '24',
       'interval_id': '100:90',
       'action': '',  
       'start': '0', #可以改变
       'limit': '20',#可以改变
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    try:
        response = requests.get(url=url, params=param, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        list_data = response.json()
        with open('./douban.json', 'w', encoding='utf-8') as fp:
            json.dump(list_data, fp=fp, ensure_ascii=False)
        print('豆瓣电影Top20数据已保存!!!!!')#用json文件查看
    except requests.RequestException as e:
        print(f'请求错误: {e}')
    except json.JSONDecodeError as e:
        print(f'JSON解析错误: {e}')