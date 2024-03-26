import re

def solve(string):
    # falta excepcionar el menos "-" y cualquier numero despues de ese menos
    math_char_list = re.findall(r"[^/-]*\d+|[+*]",string)
    print(math_char_list)
    formula = " ".join(math_char_list)
    print(formula)
    print(eval(formula))

solve(str(input("Ingrese una ecuación: ")))