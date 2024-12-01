import os, inspect
from pathlib import Path
from monedas import monedas

def leer_casos(dir):
    archivos = dir.iterdir()
    casos = {}
    for archivo in archivos:
        ind = str(archivo).rfind('/')
        nombre_arch = str(archivo)[ind+1:]
        if nombre_arch == "Resultados Esperados.txt":
            continue
        with open(archivo, 'r') as id_archivo:
            for linea in id_archivo:
                if linea[0] == '#':
                    continue
                casos[nombre_arch] = [int(x) for x in linea.strip().split(';')]
    return dict(sorted(casos.items(), key=lambda item: int(item[0].split('.')[0])))

def leer_resultados(dir):
    archivo = dir.joinpath("Resultados Esperados.txt")
    resultados = {}
    with open(archivo, 'r') as id_archivo:
        for linea in id_archivo:
            if linea[0] == '#':
                continue
            elif ".txt" in linea:
                clave = linea[:linea.rfind(".txt") + 4]
                resultados[clave] = [next(id_archivo).strip(), next(id_archivo).strip()]
    return resultados

def correr_tests(ruta):
    dir_actual = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    dir_tests = Path(dir_actual + ruta)
    casos = leer_casos(dir_tests)
    resultados = leer_resultados(dir_tests)
    for caso in casos:
        arr_sophia = []
        arr_mateo = []

        salida_esperada = resultados[caso][0]
        ganancia_esperada = resultados[caso][1]

        salida = monedas(casos[caso], arr_sophia, arr_mateo)
        ganancia = "Ganancia de Sophia: {}".format(sum(arr_sophia))

        print("Probando caso: {}".format(caso))

        assert(salida == salida_esperada)
        assert(ganancia == ganancia_esperada)

        print("Éxito en la prueba, ganancias de Sophia: {}".format(sum(arr_sophia)))
