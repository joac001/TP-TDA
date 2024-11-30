from max_coins import max_coins
import os

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
                numbers = list(map(int, line.split(';')))
    
    return numbers



def run_test(path=''):

    if path == '':
        print("Ingrese la ruta absoluta de la carpeta con los test a correr.")
        path = input("Ruta: ")
    

    test_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    out_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    obtenidos = []

    print("#"*75)
    print()
    print(f"Running test on {test_directory}")
    print("-"*75)   
    print("El resultado de este test se encuentra en el directorio out/ dentro del proyecto.")
    print("Para guardar estos resultados cambiarle el nombre al archivo de salida.\nDe lo contrario se sobreescribira.")
    print("-"*75)
    print()
    print("#"*75)

    with open(f"{out_directory}\output.txt", "w") as out_file:
        out_file.write(f"Se corrieron los tests en {test_directory}\n")
   
        for file in os.listdir(test_directory):
            if file.endswith(".txt"):
                p = os.path.join(test_directory, file)
                test_set = read_test_case(p)
                
                resultado = max_coins(test_set) # Faltaria recibir los 'steps' y el valor acumuladod de mateo.
                obtenidos.append(resultado)
                out_file.write(f"Para {test_set} se obtuvo el resultado {obtenidos[-1]}\n") # Agregar los 'steps' y el valor acumulado de mateo.
    
    out_file.close()
        
    print("\nTarea terminada.\n")
    return