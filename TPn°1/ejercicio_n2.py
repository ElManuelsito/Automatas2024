import re

def solve(string):
    

    if '(' in string or ')' in string:
        raise ValueError("La ecuación no puede contener paréntesis.")()
    
    if '-' in string:
        raise ValueError("La ecuacion no puede tener una resta")
    
    if '/' in string:
        raise ValueError("La ecuacion no puede tener una división")

    math_char_list = re.findall(r'\b(?:\d+|[+*])\b', string)  

    formula = " ".join(math_char_list)
    resultado = eval(formula)
    print("Expresión resuelta:", resultado)

<<<<<<< HEAD
solve(str(input("Ingrese una ecuación : ")))

=======
try:
    solve(str(input("Ingrese una ecuación : ")))
except ValueError as e:
    print(e)
>>>>>>> 0b0d87df03b7f748f0b3c20cbfd377ec240b1260
