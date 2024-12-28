from graficos import run_analysis
from monedas import ejecutar_desde_archivo
from tests import run_test
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

        with open("out\output.txt", "r") as archivo:
            for linea in archivo:
                print(linea, end="")


if __name__ == '__main__':
    main()