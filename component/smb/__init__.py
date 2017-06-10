KEYWORDS = ['smb', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


    if int(port) in [445] :
        return True
    else:

        return False