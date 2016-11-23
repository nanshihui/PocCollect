KEYWORDS = ['08cms', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if '08cms' in context or '08cms' in head:
		return True
	else:
		return False