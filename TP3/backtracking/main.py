from test_backtracking import run_test

import sys

def main():

    if len(sys.argv) < 2:
        print("Por favor, proporciona una ruta como argumento.")
        sys.exit(1)

    ruta = " ".join(sys.argv[1:])
    run_test(ruta)
    
    with open("../out/output.txt", "r") as archivo:
        for linea in archivo:
            print(linea, end="")



main()