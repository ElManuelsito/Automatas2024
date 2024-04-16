import re
import os
from time import sleep

os.system("")

def solve(string):
    # chequeando operadores o caracteres no admitidos
    if re.search(r'(\-|\/|\%|\#|\$|\!|\^|\?|\'|\")',  string):       
        # estos msj de advertencia normalmente irían en un CONSTANT y se mostrarían con un método, pero bueno.
        print("\n (!) Ecuación inválida. Solo se permite suma y multiplicación.")   
        sleep(3.5)
        # primer sequence mueve el cursor 1 posición arriba, el segundo borra la linea en la que éste se encuentra
        print("\x1b[1A", end="\x1b[2K")
        return solve(str(input("Ingrese una ecuación válida: ")))
    # chequeando si hay letras
    elif re.search(r'[a-zA-Z]+', string):
        print("\n (!) Ecuación inválida. Por favor no utilizar letras.")
        sleep(3.5)
        print("\x1b[1A", end="\x1b[2K")
        return solve(str(input("Ingrese una ecuación válida: ")))
    # chequeando si solo se ingresó un solo número sin nada más
    elif re.match(r'([\s]*[0-9]+[\s]*$)', string):
        print("\n (!) Ecuación inválida. Por favor ingrese una ecuación, no solo un número.")
        sleep(3.5)
        print("\x1b[1A", end="\x1b[2K")
        return solve(str(input("Ingrese una ecuación válida: ")))
    # chequeando si hay algún operador de más entre numeros para evitar un ValueError
    elif re.search(r'(^\+|\+[\s]*\+|\*[\s]*\*)+', string):
        print("\n (!) Ecuación inválida. Por favor revisa la ecuación, puede que sobre algún operador (+/*) entre números.")
        sleep(3.5)
        print("\x1b[1A", end="\x1b[2K")
        return solve(str(input("Ingrese una ecuación válida: ")))
    # chequeando si falta algún operador entre numeros para evitar un ValueError
    elif re.search(r'([0-9]+[\s]+[0-9]+)', string):
        print("\n (!) Ecuación inválida. Por favor revisa la ecuación, puede que falte algún operador (+/*) entre números.")
        sleep(3.5)
        print("\x1b[1A", end="\x1b[2K")
        return solve(str(input("Ingrese una ecuación válida: ")))
    # chequeando si falta un factor en alguna mutiplicación, ya que de ser el caso la funcion devuelve ValueError
    elif re.search(r'(\*[\s]*$|[0-9]*[\s]*\*[\s]*\+|\+[\s]*\*[\s]*[0-9]+|^[\s]*\*[\s]*[0-9]*[\s]*[\+]*)', string):
        print("\n (!) Ecuación inválida. Por favor revise la ecuación e ingrese los factores que falten.")
        sleep(3.5)
        print("\x1b[1A", end="\x1b[2K")
        return solve(str(input("Ingrese una ecuación válida: ")))
    # chequea que haya un + o * y se lleva a cabo la suma
    elif re.search(r'[+*]', string):
        char_list  = re.split(r'[+]', string)
        summation = 0
        for term in char_list:
            if re.search(r'[*]', term):
                char_list_multiplication = re.split(r'[*]', term)
                product = 1
                for factor in char_list_multiplication:
                    if int(factor).is_integer:
                        product = product * int(factor)
                summation = summation + product
            else:
                if int(term).is_integer:
                    summation = summation + int(term)
        print("\n", string, "=", summation)
    # en caso de que el input simplemente no cumpla con nada
    else:
        print("\n (!) Ecuación inválida.")
        sleep(3.5)
        print("\x1b[1A", end="\x1b[2K")
        return solve(str(input("Ingrese una ecuación válida: ")))



solve(str(input("Ingrese una ecuación (solo suma y multiplicación): ")))


# antiguo solve(), utilizando eval.

# import re

# def solve(string):

# if '(' in string or ')' in string or "-" in string:
#     raise ValueError("La ecuación no puede contener paréntesis.")()

# if '-' in string:
#     raise ValueError("La ecuacion no puede tener una resta")

# if '/' in string:
#     raise ValueError("La ecuacion no puede tener una división")

# math_char_list = re.findall(r'\b(?:\d+|[+*])\b', string)  

# formula = " ".join(math_char_list)
# resultado = eval(formula)
# print("Expresión resuelta:", resultado)
