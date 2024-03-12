def encriptar_palabra(cadena, n):
    
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    cadena_encriptada = "" 
    for letra in cadena:
        if letra in alfabeto:
            posicion = alfabeto.find(letra) 
            posicion_nueva = (posicion + n) % len(alfabeto)
            letra_nueva = alfabeto[posicion_nueva]
            cadena_encriptada += letra_nueva
        else:
            cadena_encriptada += letra
    return  cadena_encriptada

cadena = input('Seleccione la palabra para encriptar: ')

n = int(input(f'Seleccio el numero para que se desplace: '))

cadena_encriptada = encriptar_palabra(cadena, n)

print(f'La cadena encriptada es: {cadena_encriptada}')