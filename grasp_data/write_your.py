##coding=gbk
import os
import json
dic={}
dic[' ���֮���˾��й�']="https://www.69shu.com/txt/30052/26545984"
dic['��Ϊ������']='https://www.69shu.com/txt/47093/32290136'
dic['˭�������ɵģ�']='https://www.69shu.com/txt/46957/32286942'
dic[' �����已̥����������']='https://www.69shu.com/txt/47120/31443813'
with open('latest.json','w') as f:
    json.dump(dic,f)

