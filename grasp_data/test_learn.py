#抓取优美图库
#get 主页面的源代码
#get the every picture hltm
import re
import requests
import csv
from lxml import etree
tree=etree.parse()
domain='https://www.umei.cc'
url='https://www.umei.cc/katongdongman/dongmanbizhi/'
head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'}

response=requests.get(url,headers=head)
if response.status_code==200:
    print('successful get father hltm data')
else :
    print('false code ',response.status_code)
response.encoding='utf-8'
father_data=response.text
r_compile=re.compile(r'<div class="img">.*?<a href="(?P<herf>.*?)"><img class="lazy".*?alt=(?P<name>.*?) /></a>',re.S)
s=r_compile.finditer(father_data)
#get the target url
child_urls=[]
for it in s:
    child_url=domain+it.group('herf')
    child_urls.append(child_url)
downlaod_urls=[]
print(child_urls)
head2={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
for j in child_urls:
    print(j)
    child_response=requests.get(child_url,headers=head2)
    print(child_response.status_code)
    child_response.encoding='utf-8'
    if response.status_code == 200:
        print('successful get child hltm data')
    else:
        print('false code ', response.status_code)
    child_data=child_response.text
    child_re=re.compile(r'<div class="big-pic"><a href=""><p><img src="(?P<download>.*?)" alt="',re.S)
    downlaod_url=child_re.findall(child_data)
    url=downlaod_url
    print(url)
    downlaod_urls.append(url)

print(downlaod_urls)

