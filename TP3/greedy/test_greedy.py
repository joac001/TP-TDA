from batalla_naval_greedy import batalla_naval_greedy

import sys
import os
ruta_externa = os.path.abspath("../common")
sys.path.append(ruta_externa)

from test_reader import read_test_case

def run_single_test(out_file , test_set, file):
    tablero, demanda_total, demanda_cumplida, demanda_incumplida = batalla_naval_greedy (test_set[0], test_set[1], test_set[2])

    out_file.write(f"Para {file} se obtuvo:\n")
    out_file.write("Tablero: \n")
    for f in range(len(tablero)):
        for c in  range(len(tablero[f])):
            out_file.write(" "+ str(tablero[f][c]))
        out_file.write("\n")
                
    out_file.write("\n Demanda total: " + str(demanda_total))
    out_file.write("\n Demanda cumplida: " + str(demanda_cumplida))
    out_file.write("\n Demanda incumplida: " + str(demanda_incumplida))

    out_file.write("\n\n")

def mostrar_mensaje ():
    print("-"*75) 
    print("El resultado de este test se encuentra en el directorio out/ dentro del proyecto.")
    print("Para guardar estos resultados cambiarle el nombre al archivo de salida.\nDe lo contrario se sobreescribira.")
    print("-"*75)
    print()
  
def run_test(path=''):

    if path == '':
        print("Ingrese la ruta absoluta de la carpeta con los test a correr.")
        path = input("Ruta: ")
    
    out_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../out")
    with open(f"{out_directory}/output.txt", "w") as out_file:

        if (os.path.isfile(path)):
            mostrar_mensaje()
            test_set = read_test_case(path)
            if test_set == []:
                return "El archivo no respeta el formato"
            run_single_test(out_file, test_set ,path)

        elif (os.path.isdir(path)):

            test_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

            try:
                os.listdir(test_directory)
            except NotADirectoryError:
                print("\n\nLa ruta enviada no es un directorio.")
                return


            print("#"*75)
            print()
            print(f"Corriendo test en {test_directory}")
            mostrar_mensaje()
            print("#"*75)

    
            out_file.write(f"Se corrieron los tests en {test_directory}\n")
        
            for file in os.listdir(test_directory):
                if file.endswith(".txt"):
                    if file[0] == 'R': # Ignoramos los archivos de 'Resultados esperados'.
                        continue
                    p = os.path.join(test_directory, file)
                    test_set = read_test_case(p)
                    if test_set == []:
                        continue
                    run_single_test(out_file, test_set ,file)
                
                    
    
    out_file.close()
        
    print("\nTarea terminada.\n")
    return

