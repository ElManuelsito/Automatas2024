# import re

# def solve(string):
#     # falta excepcionar el menos "-" y cualquier numero despues de ese menos
#     math_char_list = re.findall(r"[^/-]*\d+|[+*]",string)
#     print(math_char_list)
#     formula = " ".join(math_char_list)
#     print(formula)
#     print(eval(formula))

# solve(str(input("Ingrese una ecuación: ")))

import re

def solve(string):
    

    if '(' in string or ')' in string:
        raise ValueError("La ecuación no puede contener paréntesis.")()
    

    if '-' in string:
        raise ValueError("La ecuacion no puede tener numero negativo")

    math_char_list = re.findall(r'\b(?:\d+|[+*])\b', string)  

    formula = " ".join(math_char_list)
    resultado = eval(formula)
    print("Expresión resuelta:", resultado)
  
try:
    solve(str(input("Ingrese una ecuación : ")))
except ValueError as e:
    print(e)