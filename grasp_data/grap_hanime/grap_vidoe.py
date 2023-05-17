#coding=utf-8
import requests
import os
from lxml import etree

url='https://hanime1.me/search?query=&type=&genre=%E8%A3%8F%E7%95%AA&sort=%E6%9C%AC%E6%9C%88%E6%8E%92%E8%A1%8C&year=&month='
headers={':authority': 'hanime1.me'
    ,'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
         ,'cookie':'__cf_bm=vJtnD9Kg7NBhFEb4K.gG5QkMiLQE6l1GfSS.NK3KT5Q-1683730061-0-ATZwMgU12ZzsZlRy71iNeCkVWzl9yb20dJqxzRejKHNviF+0ECu/emSeMDm5DUS556qmJvGsQihAtoOQXcPt3yp5o3jber997MhxeSN1B7qk; _ga=GA1.2.1544174955.1683730061; _gid=GA1.2.1093851283.1683730061; __gads=ID=a555c91fde9f765b-22dfb2a495df0073:T=1683730064:RT=1683730064:S=ALNI_MaM7fx5KiQWKxpNI7F8xDKjnOFkrA; __gpi=UID=00000bec3a1757e1:T=1683730064:RT=1683730064:S=ALNI_MaA1rYiBe6nt5jf3HU4pw5enInAQg; XSRF-TOKEN=eyJpdiI6IlNiRjFYdmZLRVwvYjBxZXlTK2ppNExnPT0iLCJ2YWx1ZSI6IjVXMzRjemJmN09WVElOeTdrZEpvYTZGT0ZjMnJTOUxXRzh3UkNUK1Y5bjF0YUNzSndWWWI4OVZJcTUwUyt3aVgiLCJtYWMiOiIzOWEyNjAyZjgzY2NiMmNkMTk3MWI3MzMzZDAyOGU5MjAwZWM1NDRlZmU2NTk0M2FkN2UxNTJkMDQ0MjA0ODE4In0%3D; hanime1_session=eyJpdiI6IlRBS1ZFc1AzR09iYzRTcWdhcmd0TVE9PSIsInZhbHVlIjoiM05PNDFNeCtsbG8xS2RLVDRHTlhcL2tKdWZVSDlPZkZLaUxwTGhzMno3UWV6cFdiR0prdHlRQ0dUK1FUU2hXdVMiLCJtYWMiOiIzODNmMTZjYjljZGU3MWE4NGQ2ZmY2NzhiYzczMWViNzJiZjUwMjRhNTY0NjlhMDljNzg1Y2U4ZTgyMmIwMTQ0In0%3D; __atuvc=4%7C19; __atuvs=645baeda327bb4ce003; _gat_gtag_UA_125786247_2=1'}

father_response=requests.get(url,headers=headers)
print(father_response.text,father_response.status_code)