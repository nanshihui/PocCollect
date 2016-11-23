KEYWORDS = ['aspcms', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'aspcms' in context or 'aspcms' in head:
		return True
	else:
		return False