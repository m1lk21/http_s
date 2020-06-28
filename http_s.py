import requests
import re


lists = []
filew = open('ok.txt','w+')
http = ['http://','https://']
for http_s in http:
    # print (http_s)
    for d in open('domain.txt','r+'):
        dom = d.strip()
        # print (http_s+dom)
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        try:
            r = requests.session()
            ru = r.get(http_s + dom,headers=header,timeout=5) #超时5s
            ru.encoding='utf-8'
            status = (ru.status_code)
            title = re.search('<title>(.*)</title>', ru.text).group(1)#获取标题
            d = (http_s+dom)
            x = '%s  ----  %s  ----  %s' % (d,status,title)
            print (x)
            lists.append(x)
            filew.write(x + "\n") #写入
        except Exception : #捕获异常
            d = (http_s+dom)
            print ("%s----连接超时" % (d))