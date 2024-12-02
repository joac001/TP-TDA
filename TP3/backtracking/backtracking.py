from backtracking.utils import *
import sys

from common.game_logic import *
from common.test_reader import *

def batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas,
                     puestos, optimos, i):
    demanda_cumplida = sum(size * 2 for (idx, size) in puestos.keys())
    demanda_optima = sum(size * 2 for (idx, size) in optimos.keys())
    if i == len(barcos):
        if demanda_cumplida > demanda_optima:
            optimos.clear()
            optimos.update({barco: pos.copy() for barco, pos in puestos.items()})
            return True
        return False

    barco = barcos[i]
    barco_idx, barco_size = barco

    alternativas = obtener_candidatos(tablero, demanda_filas, demanda_columnas, barco_size) 
    hay_alternativas = len(alternativas) > 0

    if not hay_alternativas:
        return batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas, puestos,
                                optimos, i + 1)

    proyectada = demanda_proyectada(tablero, demanda_filas, demanda_columnas, barcos, i - 1)

    if demanda_cumplida + proyectada <= demanda_optima: # No vamos a mejorar.
        return batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas, puestos,
                                optimos, i + 1)

    puestos[barco] = []
    demanda_cumplida = sum(size * 2 for (idx, size) in puestos.keys())

    for demanda, alternativa in alternativas:
        for casilleros in alternativa:
            colocar_barco(casilleros, tablero, barco_idx)
            actualizar_demandas(casilleros, demanda_filas, demanda_columnas, False)
            puestos[barco] = casilleros
            
            proyectada = demanda_proyectada(tablero, demanda_filas, demanda_columnas, barcos, i)
            buena_alternativa = demanda_cumplida + proyectada > demanda_optima
            
            if buena_alternativa:
                if batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas, 
                                    puestos, optimos, i + 1):
                    demanda_optima = sum(size * 2 for (idx, size) in optimos.keys())
            
            colocar_barco(casilleros, tablero, None) # Lo sacamos del tablero. 
            actualizar_demandas(casilleros, demanda_filas, demanda_columnas, True)

    del puestos[barco]
    k =  obtener_siguiente_distinto(barcos, i)
    
    return batalla_naval_bt(tablero, barcos, demanda_filas, demanda_columnas, puestos,
                            optimos, k)

def batalla_naval(tablero, barcos, demanda_filas, demanda_columnas):
    barcos_ordenados = list(enumerate(barcos))
    barcos_ordenados.sort(key=lambda x: -x[1])    
    optimos = {}
    batalla_naval_bt(tablero, barcos_ordenados, demanda_filas, demanda_columnas,
                     {}, optimos, 0)
    return optimos

def save_output(test_name, barcos, demanda_total):
    puestos = list(barcos.items())
    puestos.sort(key=lambda x: x[0][0])
    demanda_cumplida = 0
    with open('output.txt', 'a') as f:
        sys.stdout = f
        print(test_name)
        print('Posiciones:')
        for (barco_idx, barco_size), pos in puestos:
            demanda_cumplida += barco_size*2
            if len(pos) > 1:
                print(f"{barco_idx}: ", pos[0], " - ", pos[-1])
            else:
                print(f"{barco_idx}: ", pos[0])
        print(f"Demanda cumplida: {demanda_cumplida}")
        print(f"Demanda total: {demanda_total}\n")
    sys.stdout = sys.__stdout__