from backtracking.test_backtracking import \
     run_test as run_test_backtracking

from aproximacion.test_aproximacion import \
     run_test as run_test_aproximacion

from greedy.test_greedy import \
     run_test as run_test_greedy

BACKTRACKING = "1"
APROXIMACION = "2"
GREEDY = "3"
SALIR = "4"

GIVEN = "1"
GROUP = "2"
USER = "3"

def print_menu_general():
    print("-"*75)
    print("Tener en cuenta:\n")
    print("Se considera que las rutas que se ingresan al sistema son rutas a carpetas, no a archivos individuales,\npor lo que se intentara leer todos los archivos '.txt' que se encuentren en ese directorio.")
    print("-"*75)
    print()
    print("1. Correr test dados por la catedra.")
    print("2. Correr los test creados por el grupo.")
    print("3. Correr los test creados propios.")
    print("4. Salir.\n")

def print_menu_principal():
    print("1. Backtracking")
    print("2. Aproximacion")
    print("3. Greedy")
    print("4. Salir.\n")

def elegir_implementacion (option):

    if ((option == BACKTRACKING) or (option == APROXIMACION) or (option == GREEDY)):
        print_menu_general()
        tipo_test = input("Ingrese una opcion: ")

        if option == BACKTRACKING:
            execute_backtracking(tipo_test)
        elif option == APROXIMACION:
            execute_aproximacion(tipo_test)
        elif option == GREEDY:
            execute_greedy(tipo_test)
    
    elif option == SALIR:
        return
    else:
        print("Opcion invalida. Intente nuevamente.")

def execute_backtracking(option):
    if option == GIVEN:
        run_test_backtracking("../tests/given_tests")
    elif option == GROUP:
        run_test_backtracking("../tests/group_tests")
    elif option == USER:
        run_test_backtracking()
    elif option == SALIR:
        return
    else:
        print("Opcion invalida. Intente nuevamente.")

def execute_aproximacion(option):
    if option == GIVEN:
        run_test_aproximacion("../tests/given_tests")
    elif option == GROUP:
        run_test_aproximacion("../tests/group_tests")
    elif option == USER:
        run_test_aproximacion()
    elif option == SALIR:
        return
    else:
        print("Opcion invalida. Intente nuevamente.")

def execute_greedy(option):
    if option == GIVEN:
        run_test_greedy("../tests/given_tests")
    elif option == GROUP:
        run_test_greedy("../tests/group_tests")
    elif option == USER:
        run_test_greedy()
    elif option == SALIR:
        return
    else:
        print("Opcion invalida. Intente nuevamente.")


def main():

    print("-"*75)
    print("Bienvenido al sistema de testeo de TP3, Batalla Naval")
    print()
    print("Eliga que implementacion quiere probar:")
    print("-"*75)
    print_menu_principal()

    option = input("Ingrese una opcion: ")
    elegir_implementacion (option) 

main()