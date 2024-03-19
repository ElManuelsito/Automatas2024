import re 

def validate_string(string):
    if re.fullmatch(r"([a-zA-Z]|[0-9])?", string):
        print ('true')
    
    else:
        print ('false')

    if re.fullmatch(r"([a-zA-Z])", string):
        print ('true')
    else:
        print ('false')
    if re.fullmatch(r"([A-Z])", string):
        print ('true')
    else:
        print ('false')

    if re.fullmatch(r"([a-z])", string):
        print ('true')
    else:
        print ('false')

    if re.fullmatch(r"([0-9])", string):
        print ('true')
    else:
        print ('false')
    
    if re.fullmatch(r"({8,})", string):
        print ('true')
    else:
        print ('false')

    
    


    
print(validate_string)("JoseRUT1123123")