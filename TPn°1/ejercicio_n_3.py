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

if __name__ == "__main__":
    opcion = input("Selecciona una opción:\n1. Validar emails\n2. Validar URLs\n3. Validar direcciones IPv4\n")

    if opcion == "1":
        print("Ingrese las direcciones de correo electrónico:")
        analizar_archivo(validar_email)
    elif opcion == "2":
        print("Ingrese las URLs:")
        analizar_archivo(validar_url)
    elif opcion == "3":
        print("Ingrese las direcciones IPv4:")
        analizar_archivo(validar_direccion_ipv4)
    else:
        print("Opción inválida.")



