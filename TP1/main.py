from graficos import correr_grafico
from tests import correr_tests

RUTA_TESTS_CATEDRA = "/tests/given_tests"
RUTA_TESTS_GRUPO = "/tests/group_tests"
RUTA_TESTS_USUARIO = "/tests/user_tests"

def main():

    print("-"*75)
    print("Bienvenido al sistema de testeo de TP1.")
    print("Tener en cuenta:\nSe considera que las rutas que se ingresan al sistema son rutas a carpetas, no a archivos individuales,\npor lo que se intentara leer todos los archivos '.txt' que se encuentren en ese directorio.")
    print("-"*75)
    print()

    print_menu()
    option = input("Ingrese una opcion: ")
    execute_option(option) 

def print_menu():
    print("1. Correr test dados por la catedra.")
    print("2. Correr los test creados por el grupo.")
    print("3. Correr los test creados por mi. (Recordar ingresar los test en la carpeta 'tests/user_tests/' del proyecto)")
    print("4. Correr el gráfico de datos.")
    print("5. Salir.")

def execute_option(option):
    if option == "1":
        correr_tests(RUTA_TESTS_CATEDRA)
    elif option == "2":
        correr_tests(RUTA_TESTS_GRUPO)
    elif option == "3":
        correr_tests(RUTA_TESTS_USUARIO)
    elif option == "4":
        correr_grafico()
    elif option == "5":
        return
    else:
        print("Opcion invalida. Intente nuevamente.")

main()