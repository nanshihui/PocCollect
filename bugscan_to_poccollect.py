#!/usr/bin/env python  
import os ,random,re
import logger
logge = logger.initLog("log.log", 2, True,'a')
def readpath(path):
	rootpath=path
	files = os.listdir(path)  
	for i in xrange(len(files)):
		files[i]=rootpath+'/'+files[i]
	return files
def locatecode(path,targetpath):
	sourcepath=path
	with open(path,'r') as fileitem:
		content = fileitem.readlines()  
	func_assign_line=0
	func_audit_line=0
	func_main_line=0
	func_targetfile=None
	func_def_line=0
	params=None
	service=None
	def_line=[]
	targetpath=targetpath
	security_label=None
	targetfilepath=None
	for line in  xrange(len(content)):

		if 'curl' in content[line] and line<func_audit_line:
			error(' may fail,need change label curl not in audit ',sourcepath,targetfilepath)
		if 'def ' in content[line] :
			func_def_line=line
			def_line.append(line)
		if 'def ' in content[line] and 'assign' in content[line] and '(service' in content[line] :
			func_assign_line=line

		if 'audit' in content[line] and 'def ' in content[line] :
			prefix_params=content[line].find('(')
			suffix_params=content[line].rfind(')')
			params=content[line][prefix_params+1:suffix_params]
			if len(params)>4:
				error(' may fail,multi params ',sourcepath,targetfilepath)
			func_audit_line=line

			# writecontent(targetfilepath,content,line,len(content)-1,params,'')

		if '__name__' in content[line]:
			func_main_line=line
			def_line.append(line)
		if 'if ' in content[line] and ' service' in content[line]:
			prefix=content[line].find('"')
			suffix=content[line].rfind('"')
			service=content[line][prefix+1:suffix]
			if 'if service' in service:
				prefix=content[line].find('\'')
				suffix=content[line].rfind('\'')
				service=content[line][prefix+1:suffix]	
			index=targetpath+'/'+service
			isexit=os.path.exists(index)
			if not isexit:
				os.mkdir(index) 
			initfile=index+'/__init__.py'

			isexit=os.path.exists(initfile)
			if not isexit:
				os.mknod(initfile)
				write__init__(initfile,service)
			targetfilepath=index+'/'+service+'_'+md5(path)+'.py'
			func_targetfile=targetfilepath
		if  func_audit_line!=0 :
			match = re.search(r'security_\w+', content[line])
			if match:
				item=match.group(0)
				security_label=item
				suffix_params=content[line].rfind(')')
				labeltype=security_label.split('_')[1]
				content[line]=content[line][0:suffix_params]+',result,\''+labeltype+'\')\n'
				content[line]=content[line].replace(item,'output')
		if line>func_main_line:
			url=''
			if 'audit(assign' in content[line]:
				match=re.search(r'((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?',"""audit(assign('www','http://yunlai.cn:803/sfdsfds/')[1])""")
				if match:
					url=match.group(0)
				else:
					error(' may fail, no url ',sourcepath,targetfilepath)
				match = re.search(r'\w+',content[line])
				if match:

					t= match.group(0)

					index=content[line].find(t)
					msg=' '*index+"""print P().verify(ip='%s',port='80')\n"""%url
					content[line]=msg
				else:
					error(' may fail, no url word',sourcepath,targetfilepath)
			if 'from dummy import *' in content[line]:
				 content[line]=''
		# 	writecontent(targetfilepath,array,0,0)
	if func_assign_line==0:

		error(' may fail, no assign func',sourcepath,targetfilepath)
	path={}
	path['sourcepath']=sourcepath
	path['func_assign_line']=func_assign_line
	path['func_audit_line']=func_audit_line
	path['func_main_line']=func_main_line
	path['func_targetfile']=func_targetfile
	path['func_def_line']=func_def_line
	path['security_label']=security_label
	path['targetfilepath']=targetfilepath
	path['def_line']=def_line
	if security_label is None:
		error('  may fail, no security_label',sourcepath,targetfilepath)
	# path['func_warn_line']=func_warn_line
	# path['func_info_line']=func_info_line
	# path['func_notice_line']=func_notice_line
	path['params']=params
	path['service']=service
	if func_def_line!=func_assign_line:
		error(' may fail, have other  func',sourcepath,targetfilepath)

	return 	path,content
def error(msg,pathsrc,pathadd):
	global logge
	logge.info("info %s %s %s", "may fail, "+msg,pathsrc,pathadd)
def reform(path,targetpath):
	path_line,content=locatecode(path,targetpath)
	targetfilepath=path_line.get('func_targetfile',None)
	func_assign_line=path_line.get('func_assign_line',0)
	func_audit_line=path_line.get('func_audit_line',0)
	func_main_line=path_line.get('func_main_line',0)
	security_label=path_line.get('security_label','')
	sourcepath=path_line.get('sourcepath','')
	params=path_line.get('params','')
	def_line=path_line.get('def_line',[])

	deflist={}
	if targetfilepath:
		import_file(targetfilepath)
		writeprefix(targetfilepath,content,0,def_line[0]-1,'a')
		for i in xrange(len(def_line)):

			if def_line[i]!=func_audit_line and def_line[i]!=func_main_line and def_line[i]!=func_assign_line:
				

				writeprefix(targetfilepath,content,def_line[i],def_line[i+1]-1,'a')
			if def_line[i]==func_audit_line:
				deflist['func_audit_line']=i

			elif def_line[i]==func_main_line:
				deflist['func_main_line']=i
			elif def_line[i]==func_assign_line:
				deflist['func_assign_line']=i
		
		writeclass(targetfilepath,type='a',service=params)
		print targetfilepath,sourcepath
		print deflist
		print def_line
		if deflist['func_audit_line']+1==len(deflist):
			writeprefix(targetfilepath,content,func_audit_line+1,len(content),'a',default='    ')

		else:
			writeprefix(targetfilepath,content,func_audit_line+1,def_line[deflist['func_audit_line']+1]-1,'a',default='    ')

		writereturn(targetfilepath,type='a')
		writeoutput(targetfilepath,'a',path_line)


		
		if deflist['func_audit_line']+1==len(deflist):
			pass

		else:
			writeprefix(targetfilepath,content,func_main_line,len(content),'a')




		contents="""\n#%s\n#%s"""%(targetfilepath,sourcepath)
		writecontent(targetfilepath,contents)


def writeoutput(targetpath='',type='a',vulinfo={}):
	service=vulinfo.get('service','')
	security_label=vulinfo.get('security_label','')
	targetfilepath=vulinfo.get('func_targetfile',None)
	
	content="""

def output(url,result,label):
    info = url + '  %s  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='%s Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='%s'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

"""%(service,service,targetfilepath)
	writecontent(targetpath,content)


def writereturn(targetpath,type='a'):
	content="""
        del curl
        return result
"""
	writecontent(targetpath,content)
def writeclass(targetpath,type='w',service=''):
	content="""
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        %s='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

"""%service
	writecontent(targetpath,content,type)

def import_file(targetpath,type='w'):

	content="""from ..miniCurl import Curl
from ..t  import T
"""
	writecontent(targetpath,content,type)

def writeprefix(filepath,array,start,end,type,default=''):
	filebind = open(filepath, type)
	while end>start or end==start:
		if start==len(array) or start >len(array):
			break
		item=default+array[start]
		filebind.write(item)
		start=start+1 
	filebind.close()
def writecontent(filepath,content,type='a'):
	filebind = open(filepath, type)
	filebind.write(content)
	filebind.close() 	
def write__init__(path,service):
	content="""KEYWORDS = ['%s', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if '%s' in context or '%s' in head:
		return True
	else:
		return False""" %(service,service,service)

	targetfile=open(path,'w')
	targetfile.write(content)
	targetfile.close()
def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()   
        m.update(str)
        return m.hexdigest()
    else:
        return ''			 


if __name__ == "__main__":

	path=readpath(os.path.split(os.path.realpath(__file__))[0]+'/codesrc')

	for i in path:
		reform(i,'/root/github/poccreate/thirdparty')

	# reform('/root/github/poccreate/codesrc/exp-133.py','/root/github/poccreate/thirdparty')
	

