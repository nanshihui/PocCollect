KEYWORDS = ['edusohocms', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'edusohocms' in context or 'edusohocms' in head:
		return True
	else:
		return False