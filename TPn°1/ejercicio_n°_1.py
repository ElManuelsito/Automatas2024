import re 

def validate_string(string):
    if re.fullmatch(r"([a-zA-Z]|[0-9]){8,}?", string):
        return True
    else:
        return False
    
print(validate_string("JoseRUT1123123"))