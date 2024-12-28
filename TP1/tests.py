import os
from monedas import monedas as max_coins

'''
    Pre:    
        Se espera que la ruta enviada sea la carpeta contenedora de los archivos con los tests. 
        El archivo enviado con los test debe contener el set de numeros de la siguiente forma:
            w;x;y;...;z
        Cualquier otra linea que no se la que contenga los numeros debe comenzar con '#'.

    Pos:
        Devuelve un array 'numbers' tal que represente el set de numeros del archivo.
'''
def read_test_case(path):
    numbers = []
    
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            
            if line.startswith('#'):
                continue
            else:
                try:
                    numbers = list(map(int, line.split(';')))
                except ValueError:
                    print(f"\n\nEl archivo {path} no respeta los requisitos de los archivos de tests.\nPuedes encontrar los requisitos en el archivo READEME.md.")
                    return []
    
    return numbers

def mostrar_mensaje ():
    print("-"*75) 
    print("El resultado de este test se encuentra en el directorio out/ dentro del proyecto.")
    print("Para guardar estos resultados cambiarle el nombre al archivo de salida.\nDe lo contrario se sobreescribira.")
    print("-"*75)
    print()
 
def run_single_test (out_file, obtenidos, test_set, file):
    
    sophia = [] 
    mateo = []
    steps = max_coins(test_set, sophia, mateo)

    obtenidos.append([sophia, mateo, steps])
    out_file.write(f"Para {file} se obtuvo:\n")
    out_file.write(f"Monedas de Sophia: {sophia}\n")
    out_file.write(f"Monedas de Mateo: {mateo}\n")
    out_file.write(f"Ganancia de Sophia: {sum(sophia)}\n\n")
    out_file.write(f"Se jugo de la siguiente manera: \n")

    steps_len = len(steps)
    for step in steps:
        if step != steps[steps_len - 1]:
            out_file.write(f"{step}")
        else:
            out_file.write(f"{step}")
    out_file.write("\n\n")

def run_test(path=''):

    if path == '':
        print("Ingrese la ruta absoluta de la carpeta con los test a correr.")
        path = input("Ruta: ")
    
    out_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    obtenidos = []

    with open(f"{out_directory}/output.txt", "w") as out_file:
        
        if (os.path.isfile(path)):
            mostrar_mensaje()
            test_set = read_test_case(path)
            run_single_test(out_file, obtenidos , test_set, path)

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
                    p = os.path.join(test_directory, file)
                    test_set = read_test_case(p)
                    if test_set == []:
                        continue
                    run_single_test(out_file, obtenidos , test_set, file)
    
    out_file.close()
        
    print("\nTarea terminada.\n")
    return