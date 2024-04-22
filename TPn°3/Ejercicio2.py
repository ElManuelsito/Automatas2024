import os
from time import sleep
os.system("")

epsilon = "\u03B5"

def print_current_state(current_state, char, target_state=-1 or ""):
    if target_state != -1:
        if char == " ":
            return print(f"\n[{current_state}] -- {epsilon} -- [{target_state}]")
        else:
            return print(f"\n[{current_state}] -- {char} -- [{target_state}]")
    else:
        return print(f"\n[{current_state}] -- {char} -- [{current_state + 1}]")

def NFA_aorb_kleene_aorborempty(user_string):
    # AUTOMATA:
    # ESTADO 0 -ε-> ESTADO 1 O ESTADO 3
    # ESTADO 1 -A-> ESTADO 2
    # ESTADO 2 -ε-> ESTADO 5
    # ESTADO 3 -b-> ESTADO 4
    # ESTADO 4 -ε-> ESTADO 5
    # ESTADO 5 -a|b|ε-> ESTADO 6
    # ESTADO 6 = Aceptación
    user_char_list = list(user_string)
    current_state = 0
    if user_char_list:
        for i, char in enumerate(user_char_list):
            if (i + 1) >= len(user_char_list):
                sleep(1.5)
                if char == "a" or char == "b" or char == " ":
                    if current_state == 0:
                        print_current_state(current_state, epsilon, 5)
                        sleep(1.5)
                    print_current_state(5, char, 6)
                    sleep(1.5)
                    return print("\nCadena aceptada\n")
                else:
                    sleep(1.5)
                    return print("\nCadena NO aceptada\n")
            else:
                while True:
                    sleep(1.5)
                    if current_state == 0 and char == "a":
                        print_current_state(current_state, epsilon)
                        current_state = 1
                        continue
                    elif current_state == 1 and char == "a":
                        print_current_state(current_state, char)
                        sleep(1.5)
                        print_current_state(current_state + 1, epsilon, 5)
                        current_state = 5
                        break
                    elif current_state == 5 and char == "a":
                        print_current_state(current_state, epsilon, 0)
                        current_state = 0
                        continue
                    elif current_state == 0 and char == "b":
                        print_current_state(current_state, epsilon, 3)
                        current_state = 3
                        continue
                    elif current_state == 3 and char == "b":
                        print_current_state(current_state, char)
                        sleep(1.5)
                        print_current_state(current_state + 1, epsilon, 5)
                        current_state = 5
                        break
                    elif current_state == 5 and char == "b":
                        print_current_state(current_state, epsilon, 0)
                        current_state = 0
                        continue
                    elif current_state == 0 and char == " ":
                        print_current_state(current_state, char, 5)
                        current_state = 5
                        break
                    elif current_state == 5 and char == " ":
                        print_current_state(current_state, char, 0)
                        current_state = 0
                        continue
                    else:
                        return print("\nCadena NO aceptada\n")
    else:
        print_current_state(0, epsilon, 5)
        sleep(1)
        print_current_state(5, epsilon, 6)
        sleep(1)
        return print("\nCadena aceptada\n")
    return

def DFA_aorb_kleene_aorborempty(user_string):
    # AUTOMATA:
    # ESTADO A (aceptación) |-a-> ESTADO B
    #                       |-b-> ESTADO C
    #
    # ESTADO B (aceptación) |-a-> ESTADO B
    #                       |-b-> ESTADO C 
    #
    # ESTADO C (aceptación) |-a-> ESTADO B
    #                       |-b-> ESTADO C
    user_char_list = list(user_string)
    current_state = "A"
    if user_char_list:
        for i, char in enumerate(user_char_list):
            while True:
                sleep(1.5)
                if current_state == "A" and char == "a":
                    print_current_state(current_state, char, "B")
                    if (i + 1) >= len(user_char_list):
                        sleep(1.5)
                        return print("\nCadena aceptada\n")
                    else:
                        current_state = "B"
                        break
                elif current_state == "A" and char == "b":
                    print_current_state(current_state, char, "C")
                    if (i + 1) >= len(user_char_list):
                        sleep(1.5)
                        return print("\nCadena aceptada\n")
                    else:
                        current_state = "C"
                        break
                elif current_state == "B" and char == "a":
                    print_current_state(current_state, char, current_state)
                    if (i + 1) >= len(user_char_list):
                        sleep(1.5)
                        return print("\nCadena aceptada\n")
                    else:
                        current_state = current_state
                        break
                elif current_state == "B" and char == "b":
                    print_current_state(current_state, char, "C")
                    if (i + 1) >= len(user_char_list):
                        sleep(1.5)
                        return print("\nCadena aceptada\n")
                    else:
                        current_state = "C"
                        break
                elif current_state == "C" and char == "a":
                    print_current_state(current_state, char, "B")
                    if (i + 1) >= len(user_char_list):
                        sleep(1.5)
                        return print("\nCadena aceptada\n")
                    else:
                        current_state = "B"
                        break
                elif current_state == "C" and char == "b":
                    print_current_state(current_state, char, current_state)
                    if (i + 1) >= len(user_char_list):
                        sleep(1.5)
                        return print("\nCadena aceptada\n")
                    else:
                        current_state = current_state
                        break
                elif char == " ":
                    print_current_state(current_state, epsilon, current_state)
                    if (i + 1) >= len(user_char_list):
                        sleep(1.5)
                        return print("\nCadena aceptada\n")
                    else:
                        current_state = current_state
                        break
                else:
                    return print("\nCadena NO aceptada\n")
    else:
        print_current_state(current_state, epsilon, current_state)
        sleep(1)
        return print("\nCadena aceptada\n")
    return

def show_FSM_options():
    print("Seleccione un tipo de automata\n1. AFN\n2. AFD")
    while True:
        user_fsm_choice = input("Opción: ")
        if user_fsm_choice == "1":
            sleep(0.7)
            return NFA_aorb_kleene_aorborempty(str(input("\nIngrese una expresión: ")))
        elif user_fsm_choice == "2":
            sleep(0.7)
            return DFA_aorb_kleene_aorborempty(str(input("\nIngrese una expresión: ")))
        else:
            print(" (!) Opción no valida")
            sleep(2)
            print("\x1b[1A", end="\x1b[2K")
            print("\x1b[1A", end="\x1b[2K")


show_FSM_options()
