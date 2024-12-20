from tests_module import run_test
from complexity_analysis import run_analysis

def main():

    print("-"*75)
    print("Bienvenido al sistema de testeo de TP2.")
    print("Tener en cuenta:\nSe considera que las rutas que se ingresan al sistema son rutas a carpetas, no a archivos individuales,\npor lo que se intentara leer todos los archivos '.txt' que se encuentren en ese directorio.")
    print("-"*75)
    print()

    print_menu()
    option = input("Ingrese una opcion: ")
    execute_option(option) 

def print_menu():
    print("1. Correr test dados por la catedra.")
    print("2. Correr los test creados por el grupo.")
    print("3. Correr los test creados por mi.")
    print("4. Analisis de complejidad.")
    print("5. Salir.\n")


def execute_option(option):
    if option == "1":
        run_test("tests/given_tests")
    elif option == "2":
        run_test("tests/group_tests")
    elif option == "3":
        run_test()
    elif option == "4":
        run_analysis()
    elif option == "5":
        return
    else:
        print("Opcion invalida. Intente nuevamente.")

main()