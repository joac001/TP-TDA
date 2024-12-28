from tests_module import run_test
from complexity_analysis import run_analysis
import sys

def main():

    if len(sys.argv) < 2:
        print("Por favor, proporciona una ruta como argumento.")
        sys.exit(1)

    if (sys.argv[1] == "analisis"):
        run_analysis()
    else:
        ruta = " ".join(sys.argv[1:])
        run_test(ruta)
    
        with open("out/output.txt", "r") as archivo:
            for linea in archivo:
                print(linea, end="")



main()