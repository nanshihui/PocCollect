KEYWORDS = ['huaficms', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'huaficms' in context or 'huaficms' in head:
		return True
	else:
		return False