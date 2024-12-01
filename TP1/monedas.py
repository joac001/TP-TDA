import os, inspect

RUTA_SALIDA = "/out/output.txt"

def escribir_salida(texto, ganancia):
    dir_actual = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    with open(dir_actual + RUTA_SALIDA, 'w+') as archivo:
        archivo.write(texto + "\n")
        archivo.write("Ganancia de Sophia: " + str(ganancia) + "\n")

def ejecutar_desde_archivo(ruta):
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            if linea[0] == '#':
                continue
            arr = [int(x) for x in linea.strip().split(';')]
    arr_soph = []
    escribir_salida(monedas(arr, arr_soph, []), sum(arr_soph))
    print("Proceso finalizado. Resultados en /out/output.txt")

def monedas(arr, arr_soph, arr_mat):
    izq = 0
    der = len(arr) - 1
    res = ""
    for i in range(len(arr)):
        prim = arr[izq]
        ult = arr[der]
        if i % 2 == 0:
            if prim > ult:
                res += "Primera moneda para Sophia; "
                arr_soph.append(prim)
                izq += 1
            else:
                res += "Última moneda para Sophia; "
                arr_soph.append(ult)
                der -= 1
        else:
            if arr[izq] < arr[der]:
                res += "Primera moneda para Mateo; "
                arr_mat.append(prim)
                izq += 1
            else:
                res += "Última moneda para Mateo; "
                arr_mat.append(ult)
                der -= 1
    return res[:-2]
