import requests
import random
import re
import urllib3
print("""
#-------------------bt批量检测小脚本---------------------#
                                                    by:whitekami@foxmail.com
    """)
urllib3.disable_warnings()
user_agent = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)'
]
headers = {
    "User-Agent": random.choice(user_agent),
    "Content-Type":"application/x-www-form-urlencoded",
    'Connection': 'close'
}
for line in open('url.txt','r'):
    line=line.rstrip("\n")
    if line.strip():
        url = line+"/pma"
    try:
        geturl = requests.get(url=url,headers=headers,timeout=3,verify=False)
        html = geturl.text
        status=geturl.status_code
        pattern =re.findall(r'phpMyAdmin(.*)</title>',html)
        for t in pattern:
            fo = open('bt.txt', "ab+")
            fo.write((url+' phpMyAdmin'+t+'存在漏洞'+'\n').encode('UTF-8'))
            fo.close()
        if status == 200:
            print("此网站存在漏洞{}".format(url)+" phpMyAdmin"+str(pattern))
            pass
        else:
            print("{} 此网站不存在漏洞".format(url))
    except Exception as e:
        print('{} 网站无法访问'.format(url))
        