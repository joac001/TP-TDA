from utils import *

import sys
import os
ruta_externa = os.path.abspath("../common")
sys.path.append(ruta_externa)

from test_reader import *

def aproximacion_batalla_naval(tablero, demanda_filas, demanda_columnas, barcos):
    barcos_ordenados = ordenar_barcos(barcos)
    puestos = {}
    demandas = referenciar_demandas(demanda_filas, demanda_columnas)
    while (len(demandas) > 0 and len(puestos) < len(barcos)):
        hubo_inserciones = False
        (idx, tipo_demanda), demanda = max(demandas.items(), key=lambda x: x[1])
        for barco in barcos_ordenados:     
            barco_idx, barco_size = barco
            if (barco_size > demanda or barco in puestos):
                continue
            if tipo_demanda == FILA:
                alternativa = obtener_alternativa(tablero, demanda_columnas, COLUMNA, idx, barco_size)
            else:
                alternativa = obtener_alternativa(tablero, demanda_filas, FILA, idx, barco_size)
            if (len(alternativa) == 0):
                continue
            # -------------------- Colocamos un barco --------------------
            colocar_barco(alternativa, tablero, barco_idx)
            actualizar_demandas(alternativa, demanda_filas, demanda_columnas, False)
            puestos[barco] = alternativa
            hubo_inserciones = True
            # ------------------- Actualizamos demandas -------------------
            demandas[(idx, tipo_demanda)] -= barco_size
            if tipo_demanda == FILA:
                disminuidos_idx = list(map(lambda x: x[1], alternativa)) 
                disminuidos = [(x, COLUMNA) for x in disminuidos_idx]
            else:
                disminuidos_idx = list(map(lambda x: x[0], alternativa))
                disminuidos = [(x, FILA) for x in disminuidos_idx]
            for disminuido in disminuidos:
                if disminuido in demandas: 
                    demandas[disminuido] -= 1
            break
        if not hubo_inserciones:
            del demandas[(idx, tipo_demanda)]
    return puestos

def save_output(test_name, barcos, demanda_total, f):
    puestos = list(barcos.items())
    puestos.sort(key=lambda x: x[0][0])
    demanda_cumplida = 0
    
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
    print(f"Demanda incumplida: {demanda_total}\n")
    sys.stdout = sys.__stdout__