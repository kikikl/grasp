##coding=gbk
import os
import json
dic={}
dic[' 咫尺之间人尽敌国']="https://www.69shu.com/txt/30052/26545984"
dic['我为长生仙']='https://www.69shu.com/txt/47093/32290136'
dic['谁让他修仙的！']='https://www.69shu.com/txt/46957/32286942'
dic[' 从肉体凡胎到粉碎星球']='https://www.69shu.com/txt/47120/31443813'
with open('latest.json','w') as f:
    json.dump(dic,f)

