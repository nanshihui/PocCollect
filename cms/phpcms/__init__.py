KEYWORDS = ['phpcms', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'phpcms' in context or 'phpcms' in head:
		return True
	else:
		return False