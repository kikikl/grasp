#coding=utf-8
import re
import requests
def send_status(response):
    if response.status_code == 200:
        print('successful get the hltm')
    else :
        print('Fail to get the hltm {}'.format(response.status))

def response_encode(response):
    response.encoding='utf-8'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'}
domain='https://www.umei.cc'
#get the father url code
father_url='https://www.umei.cc/katongdongman/dongmanbizhi/'
father_response=requests.get(father_url,headers=headers)
send_status(father_response)
response_encode(father_response)
father_text=father_response.text
#get child url suffix
child_suffixs=re.compile(r'<div class="img">.*?<a href="(?P<herf>.*?)"><img class="lazy".*?alt=(?P<name>.*?) /></a>',re.S).finditer(father_text)
child_urls=[]
names=[]
for suffix in child_suffixs:
    """get the total chiild url"""
    child_url=domain+suffix.group('herf')
    child_urls.append(child_url)
    # names.append(domain+suffix.group('name'))
download_urls=[]
for child_url in child_urls[:]:
    print(child_url)
    child_response=requests.get(child_url,headers=headers)
    send_status(child_response)
    response_encode(child_response)
    child_text=child_response.text
    download=re.compile(r'<div class="big-pic"><a href=".*?"><p><img src="(?P<download>.*?)" alt=.*?" title="(?P<name>.*?)"></p></a></div>',re.S).findall(child_text)[0][0]
    name=re.compile(r'<div class="big-pic"><a href=".*?"><p><img src="(?P<download>.*?)" alt=.*?" title="(?P<name>.*?)"></p></a></div>',re.S).findall(child_text)[0][1][:5]
    print(download)
    download_urls.append(download)
    names.append(name)

print(download_urls,names)
#save the picture
with open('pic.csv','w') as f1:
    for i in range(len(names)):
        f1.write(names[i]+'\t'+download_urls[i]+'\n')

for id,download_url in enumerate(download_urls):
    download_response=requests.get(download_url,headers=headers)
    with open('{}.jpg'.format(names[id]),'wb',encoding='utf-8') as f:
        f.write(download_response.content)
        print('{} has been downlaoded and save'.format(names[id]))