from certificador_batalla_naval import certificador_batalla_naval

import os

def read_test_case(path):
    ''' 
    fields[0] -> Demanda por fila
    fields[1] -> Demanda por columna
    fields[2] -> Tamaño de cada barco
    fields[3] -> Tablero
    '''
    with open(path, "r") as archivo:
        # Leer y dividir por secciones en base a líneas vacías
        contenido = archivo.read().strip().split("\n\n")
        
        # Procesar cada sección
        lista1 = [int(x) for x in contenido[0].split()]
        lista2 = [int(x) for x in contenido[1].split()]
        lista3 = [int(x) for x in contenido[2].split()]
        matriz = [[int(num) for num in linea.split()] for linea in contenido[3].splitlines()]
        
    return lista1, lista2, lista3, matriz




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

    print("#"*75)
    print()
    print(f"Corriendo test en {test_directory}")
    print()
    print("#"*75)

    for file in os.listdir(test_directory):
        if file.endswith(".txt"):
            p = os.path.join(test_directory, file)
            filas, columnas, barcos, tablero = read_test_case(p)
            if ((not filas) or (not columnas) or (not barcos) or (not tablero)) :
                continue

            print (f"\nPara {file} se obtuvo:")                
            if (certificador_batalla_naval (tablero, barcos, filas, columnas)):
                print ("La solucion es valida.")
            else:
                print("La solucion no es valida.")
        
    print("\nTarea terminada.\n")
    return

