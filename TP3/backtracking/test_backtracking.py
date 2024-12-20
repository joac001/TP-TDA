from backtracking.backtracking import batalla_naval, save_output
from common.test_reader import read_test_case
import os

def run_test(path=''):

    if path == '':
        print("Ingrese la ruta absoluta de la carpeta con los test a correr.")
        path = input("Ruta: ")
    

    test_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    
    try:
        os.listdir(test_directory)
    except NotADirectoryError:
        print("\n\nLa ruta enviada no es un directorio.")
        return

    out_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../out")

    print("#"*75)
    print()
    print(f"Corriendo test en {test_directory}")
    print("-"*75)   
    print("El resultado de este test se encuentra en el directorio out/ dentro del proyecto.")
    print("Para guardar estos resultados cambiarle el nombre al archivo de salida.\nDe lo contrario se sobreescribira.")
    print("-"*75)
    print()
    print("#"*75)

    with open(f"{out_directory}/output.txt", "w") as out_file:
        out_file.write(f"Se corrieron los tests en {test_directory}\n")
        
        for file in os.listdir(test_directory):
            if file.endswith(".txt"):
                if file[0] == 'R': # Ignoramos los archivos de 'Resultados esperados'.
                    continue
                p = os.path.join(test_directory, file)
                test_set = read_test_case(p)
                if test_set == []:
                    continue
                
                tablero = [[None for _ in range(len(test_set[1]))] for _ in range(len(test_set[0]))]
                puestos = batalla_naval(tablero, test_set[2], test_set[0], test_set[1])
                save_output(file, puestos, sum(test_set[0]) + sum(test_set[1]), out_file)
                
                out_file.write("\n\n")
    
    out_file.close()
        
    print("\nTarea terminada.\n")
    return

