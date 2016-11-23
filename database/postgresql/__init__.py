KEYWORDS = ['postgresql', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'postgresql' in context or 'postgresql' in head:
		return True
	else:
		return False