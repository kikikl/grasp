#获取他们都在看的名字以及下载地址
#其都在源码可获得
#1.先获取他们都在看的页面源码
#2.获取源码中他们的名字以及相应的链接
#3.获取进入的链接下载地址以及评论？介绍

import re
import requests
headers={
'cookie': '__gads=ID=83b5fb2d1db945ae-2295813693df00c0:T=1683696920:RT=1683696920:S=ALNI_MYTHK4MZDxF0nCRXH8BnRt9uyDjiQ; __gpi=UID=00000bec2080db0a:T=1683696920:RT=1683696920:S=ALNI_MbTmcvcQaru44gv3Rr4K79k1MU4Kw; _ga=GA1.2.1350842107.1683696917; _gid=GA1.2.1954232059.1683696918; __atuvc=1|19; __atuvs=645b2f340ca862f4000; __cf_bm=k_DEORuQ_qh98bxMuWw7k5jHpFSMH.LV9A8visJyg0Q-1683697466-0-AQRtNT/CBxmWg8oIfVy0sqIhDYdUmvnWF8w6xC38yeDrc96PDkh6uUTZFHg6OBeSfMbtzo0vgNtUSQu/SP/WyBbUTuDJ+r1n+c+DiadGOFg5; XSRF-TOKEN=eyJpdiI6Im5hdzRTNTJoN0hTaTgxUWwyeGUzTlE9PSIsInZhbHVlIjoieFJleWNZcXNpRUdjQ3FVSU1tS3NyUnRJZVFUcEhiY3pNQ3BBNEFLOEpTaW51VWM5SGI4YmVlWjZCaitCZlAxVCIsIm1hYyI6IjZjYmQ3NjkxYjlkYjQ1YmVjNzFkNGFiMzkzNzMxNDljMThjMDk4MzdhOWU5ZDIxNzgwZWY5OGJhNDBjNmU1NzkifQ==; hanime1_session=eyJpdiI6IlwvSUltdHJ1RVpxeXlnd2VndjlWMWxBPT0iLCJ2YWx1ZSI6ImJEeGlpNnhGU05WNmxXUjFLZFRCMVdyN1RPMDM4NXJSazl5SG1OdzEyTXFoOFc1Umc1QVJmVk04Unc2NDJ4dW4iLCJtYWMiOiJlMGI3N2U3YTE2ODBlY2IyM2M1Y2U4NWE5MjdlMzRmMTY5ZDJjMDI0NGNiM2IzYzNiYTM0YjNjYjI3NWEyZmZkIn0=; _gat_gtag_UA_125786247_2=1'
,
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
,'upgrade-insecure-requests': '1'}

url='https://hanime1.me'
result=requests.get(url,headers=headers)
print(result.status_code)