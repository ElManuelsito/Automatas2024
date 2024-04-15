import re
import sys

def validar_email(email):
    patron = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_url(url):
    patron = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[^\s?]*)?(\?\S*)?$'
    return re.match(patron, url) is not None

def validar_direccion_ipv4(ip):
    # Expresión regular para validar la dirección IPv4
    patron = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(patron, ip) is not None

def analizar_archivo(validador):
    for linea in sys.stdin:
        if validador(linea.strip()):
            print(f"'{linea.strip()}' es válido.")
        else:
            print(f"'{linea.strip()}' no es válido.")

def leer_opciones_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return [linea.strip() for linea in archivo]

if __name__ == "__main__":
    opciones = leer_opciones_desde_archivo('opcion.txt')

    if len(opciones) < 3:
        print("El archivo no contiene suficientes líneas.")
    else:
        print("Validando correo electrónico:", opciones[0])
        if validar_email(opciones[0]):
            print("El correo electrónico es válido.")
        else:
            print("El correo electrónico no es válido.")

        print("Validando URL:", opciones[1])
        if validar_url(opciones[1]):
            print("La URL es válida.")
        else:
            print("La URL no es válida.")

        print("Validando dirección IPv4:", opciones[2])
        if validar_direccion_ipv4(opciones[2]):
            print("La dirección IPv4 es válida.")
        else:
            print("La dirección IPv4 no es válida.")


