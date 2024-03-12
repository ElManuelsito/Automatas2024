# Nombres e/o Indicaciones: oraciones que le indiquen al usuario donde está y/o qué hacer
MAIN_MENU = "\n\t\t\t\tEncriptador de texto\nPor favor, seleccione uno de los métodos de encriptado\n"
REQUEST_USER_STRING = "\nPor favor ingrese una cadena de caracteres: "
REQUEST_USER_POSITIONS_TO_MOVE = "Por favor ingrese la cantidad de posiciones a mover: "

# Opciones: textos que contengan '1.', '2.' etc. o que soliciten al usuario confirmar su selección
CONFIRM_CHOICE = "\nOpción: "
CONFIRM_CHOICE_YES_OR_NO = "\n¿Desea continuar? (si/no)\nOpción: "
MAIN_MENU_OPTIONS = "1. Reemplazar carácter por otro en N posiciones"

# Descripciones: oraciones que expliquen cómo opera cada método de encriptado disponible
ENCRYPT_CHAR_BY_N_POSITIONS_DESC = ("\nDescripción:\nSimple encriptado que reemplaza cada letra de su cadena\n"
                                    "por la letra que esté \033[1mn\033[0m posiciones más adelante en el abecedario")

# Componentes o elementos necesarios para el funcionamiento de los métodos de encriptado o del menu
TIME_BETWEEN_WARNINGS = 2
TIME_BETWEEN_MESSAGES = 1
SPANISH_ALPHABET_LOWERCASE = "abcdefghijklmnñopqrstuvwxyz"
SPANISH_ALPHABET_LOWERCASE_TILDE = "ábcdéfghíjklmnñópqrstúvwxyz"
SPANISH_ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
SPANISH_ALPHABET_UPPERCASE_TILDE = "ÁBÉFÍJÓPÚV"
USER_SET_FOR_YES = {"s", "S", "si", "sí", "SI", "SÍ", "Si", "Sí", "sI", "sÍ", "y", "Y", "yes", "Yes", "YES"}
USER_SET_FOR_NO = {"no", "No", "NO", "nO", "n", "N"}

# Advertencias o avisos
SUCCESSFUL_ENCRYPTION = "\nLa cadena ha sido encriptada exitosamente:"
WARNING_INVALID_YES_OR_NO_CHOICE = " (!) Por favor ingrese sí o no"
WARNING_INVALID_CHOICE = " (!) Por favor ingrese una opción válida"

# print(MAIN_MENU)
# print(MAIN_MENU_OPTIONS)
# print(CONFIRM_CHOICE)
# print(ENCRYPT_CHAR_BY_N_POSITIONS_DESC)
# print(CONFIRM_CHOICE_YES_OR_NO)

# for char in SPANISH_ALPHABET_LOWERCASE:
#     print(ord(char))
# print("\n\n")
# for char in SPANISH_ALPHABET_UPPERCASE:
#     print(ord(char))
# print("\n\n")
# for char in SPANISH_ALPHABET_LOWERCASE_TILDE:
#     print(ord(char))
# print("\n\n")
# for char in SPANISH_ALPHABET_UPPERCASE_TILDE:
#     print(ord(char))