#coding=gbk
import json
import re
import requests
from lxml import etree
import os

with open('latest.json','r') as f:
       latest_url_data=json.load(f)
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'}
flag='htt'
all_chapter_link=[]
for name , url in latest_url_data.items():
    print(f'succeful get the {name} latest url {url}')
    novel_response = requests.get(url, headers=headers)
    if 'http' not in url:
        print("over!!已经到达最新章节{}")
        continue
    if novel_response.status_code == 200:
        novel_response.encoding = 'gbk'
        novel_data = novel_response.text
        tree = etree.HTML(novel_data)

        result_text = tree.xpath('/html/body/div[3]/div/div[3]/text()')
        next_chapter = tree.xpath('/html/body/div[3]/div/div[4]/a[4]/@href')
        chapter_name = tree.xpath('/html/body/div[3]/div/div[3]/h1/text()')[0]
    url = next_chapter[0]
    while True:
        if 'http' not in url :
            print("over!!已经到达最新章节{}".format(chapter_name))
            break
        novel_response = requests.get(url, headers=headers)
        if novel_response.status_code==200:
            novel_response.encoding='gbk'
            novel_data=novel_response.text
            tree=etree.HTML(novel_data)

            result_text=tree.xpath('/html/body/div[3]/div/div[3]/text()')
            next_chapter=tree.xpath('/html/body/div[3]/div/div[4]/a[4]/@href')
            chapter_name=tree.xpath('/html/body/div[3]/div/div[3]/h1/text()')[0]
        url=next_chapter[0]
        with open(f'{name}.txt','a',encoding='gbk') as f:
            for i in result_text:
                f.write(i.strip()+'\n')
        print(f'已保存{chapter_name}')
        if 'http' not in url :
            print("over!!已经到达最新章节{}".format(chapter_name))
            break
        latest_url_data[f'{name}']=url
        with open('latest.json','w',encoding='gbk') as f:
            json.dump(latest_url_data,f)

