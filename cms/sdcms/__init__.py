KEYWORDS = ['sdcms', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'sdcms' in context or 'sdcms' in head:
		return True
	else:
		return False