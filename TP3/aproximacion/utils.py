FILA = 0
COLUMNA = 1

import sys

common_directory_path = '../common/'
sys.path.append(common_directory_path)
from game_logic import *

def ordenar_barcos(barcos):
    referencia_barcos = list(enumerate(barcos))
    referencia_barcos.sort(key=lambda x: -x[1])
    return referencia_barcos

def referenciar_demandas(demanda_filas, demanda_columnas):
    referencias = {}
    for idx, demanda_fila in enumerate(demanda_filas):
        referencias[(idx, FILA)] = demanda_fila
    for idx, demanda_columna in enumerate(demanda_columnas):
        referencias[(idx, COLUMNA)] = demanda_columna
    return referencias

def obtener_alternativa(tablero, demandas, tipo_demanda, demanda_idx, barco_size):
    alternativa = []
    consecutivos = 0
    idx_inicial = 0
    idx_final = None

    for x in range(len(demandas)):
        if demandas[x] == 0:
            idx_inicial = x + 1
            consecutivos = 0
            continue

        if (tipo_demanda == COLUMNA and hay_adyacencias(demanda_idx, x, tablero)) \
        or (tipo_demanda == FILA and hay_adyacencias(x, demanda_idx, tablero)):
            idx_inicial = x + 1
            consecutivos = 0
            continue

        consecutivos += 1
        if consecutivos == barco_size:
            idx_final = x
            break
    
    if idx_final is not None:
        for x in range(idx_inicial, idx_final + 1):
            if tipo_demanda == COLUMNA:
                alternativa.append((demanda_idx, x))
            elif tipo_demanda == FILA:
                alternativa.append((x, demanda_idx))
    
    return alternativa
