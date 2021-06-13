# -*- codeing = utf-8 -*-
# @Author : 96bearli
'''
献丑啦，用Python自给自足[流汗滑稽]
手机写的，如有错误欢迎指正
和保存的请求体在同一目录运行即可
会打印代码并保存到同一目录的req.py
'''
import json
with open('./request.json','r') as f:
    req_json = json.load(f)
headers = req_json['headers']
url = req_json['url']

if 'POST' in req_json['method']:
    try:
        f = open('./request_body.bin','r')
        data = f.read()
        f.close()
    except Exception as error:
        print("#注意：post请求的data文件request_body.bin不存在")
        data = ""
    code='''import requests
headers = %s
url = "%s"
data = "%s"
req = requests.post(url=url,headers=headers,data=data,timeout=3)
print(req.text)
    '''%(headers,url,data.replace('\"','\\"'))
else:
    code='''import requests
headers = %s
url = "%s"
req = requests.get(url=url,headers=headers,timeout=3)
print(req.text)
    '''%(headers,url)
print(code)
with open('./req.py','w') as f:
    f.write(code)
