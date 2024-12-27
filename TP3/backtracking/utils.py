
import sys
import os
ruta_externa = os.path.abspath("../common")
sys.path.append(ruta_externa)

from game_logic import hay_adyacencias 

'''
    Pre: 'demandas' es un array con los valores de las demandas que
         tiene una fila/columna.
    
    Pos: Devuelve un array con cada indice i de 'demandas' tal que
         se cumple que demandas[i] >= barco_size.
'''
def obtener_candidatos_por_demanda(demandas, barco_size):
    candidatos = []
    for i, demanda in enumerate(demandas):
        if demanda >= barco_size:
            candidatos.append(i)
    return candidatos
        
''' 
    Pre: 'columnas_disponibles' es una lista con indices de columnas
         del tablero cuya demanda es >= k.
         'f' es el indice de una fila en el tablero.

    Pos: Devuelve una lista de grupos de k puntos, todos los puntos
         que esten en un mismo grupo van a estar en la misma fila f. 
         (fila f fija, columna c_i variable para cada punto de un grupo).

         Cada punto de un mismo grupo es adyacente con el anterior
         (i.e. a (f, c_i - 1)) y con el siguiente (f, c_i + 1).

         (Cada grupo de puntos representa un lugar en el tablero
          en donde podemos poner un barco de tamaño k)
'''
def posiciones_para_barco_por_fila(columnas_disponibles, f, k, todas = True):
    if len(columnas_disponibles) < k:
        return []
    
    casilleros = []
    for c in columnas_disponibles:
        casilleros.append((f, c))
    
    posiciones = []
    for i in range(len(casilleros) - k + 1):
        son_consecutivos = True
        consecutivos = []
        for j in range(k):
            actual = casilleros[i + j]
            consecutivos.append(actual)
            if j >= k - 1:
                continue

            siguiente = casilleros[i + j + 1]
            if actual[1] + 1 != siguiente[1]:
                son_consecutivos = False
        
        if son_consecutivos:
            posiciones.append(consecutivos.copy())
            
            if not todas:
                # Devolvemos una sola posicion.
                return posiciones
        son_consecutivos = False

    return posiciones

'''
    Pre: 'filas_disponibles' es una lista con indices de filas del
         tablero cuya demanda es >= k.
         'c' es el indice de una columna en el tablero.

    Pos: Devuelve una lista de grupos de k puntos, todos los puntos 
         que esten en un mismo grupo van a estar en la misma columna c.
         (columna c fija, fila f_i variable).

         Cada punto de un mismo grupo es adyacente con el anterior
         (i.e. a (f_i - 1, c)) y con el siguiente (f_i + 1, c).

         (Cada grupo de puntos representa un lugar en el tablero
          en donde podemos poner un barco de tamaño k)
'''
def posiciones_para_barco_por_columna(filas_disponibles, c, k, todas = True):
    if len(filas_disponibles) < k:
        return []
    
    casilleros = []
    for f in filas_disponibles:
        casilleros.append((f, c))
    
    posiciones = []
    for i in range(len(casilleros) - k + 1):
        son_consecutivos = True
        consecutivos = []
        for j in range(k):
            actual = casilleros[i + j]
            consecutivos.append(actual)
            if j >= k - 1:
                continue

            siguiente = casilleros[i + j + 1]
            if actual[0] + 1 != siguiente[0]:
                son_consecutivos = False
        
        if son_consecutivos:
            posiciones.append(consecutivos.copy())

            if not todas:
                # Devolvemos una sola posicion.
                return posiciones
        son_consecutivos = False

    return posiciones

def guardar_nuevos_candidatos(demanda, candidatos, nuevos_candidatos):
    if len(nuevos_candidatos) == 0:
        return

    if not demanda in candidatos:
        candidatos[demanda] = []

    for lista in nuevos_candidatos:
        candidatos[demanda].append(lista)

'''
    Pos: Devuelve una lista de tuplas.
         
         Cada tupla contiene informacion de la forma (demanda, posiciones_candidatas),
         en donde 'demanda' es un entero relacionada con linea del tablero (fila o 
         columna) y 'posiciones_candidatas' es una lista de listas con grupos de puntos
         (x_i, y_i) que podria ocupar el barco si lo ubicamos en el tablero.
         
         Los puntos en cada grupo de puntos son posiciones validas, es decir, no exceden
         a la demanda de ninguna fila ni columna, ni son adyacentes con ningun casillero
         que otro barco este ocupando en el tablero.
'''
def obtener_candidatos(tablero, demanda_filas, demanda_columnas, barco_size, todos = True):
    candidatos_fila = obtener_candidatos_por_demanda(demanda_filas, barco_size)
    posiciones_candidatas = {}

    for f in candidatos_fila:
        columnas_disponibles = []
        for c in range(len(demanda_columnas)):
            if demanda_columnas[c] == 0 or tablero[f][c] != None:
                continue
            elif not hay_adyacencias(f, c, tablero):
                columnas_disponibles.append(c)
        demanda = demanda_filas[f]
        nuevos_candidatos = posiciones_para_barco_por_fila(columnas_disponibles, f, barco_size, todos)
        guardar_nuevos_candidatos(demanda, posiciones_candidatas, nuevos_candidatos)
        if not todos and len(nuevos_candidatos) > 0:
            return list(posiciones_candidatas.items())
    
    # Para que no se dupliquen los candidatos si un barco ocupa 1 casillero.
    if (barco_size == 1):
        return list(posiciones_candidatas.items())
    candidatos_columna = obtener_candidatos_por_demanda(demanda_columnas, barco_size)
    
    for c in candidatos_columna:
        filas_disponibles = []
        for f in range(len(demanda_filas)):
            if ((demanda_filas[f] == 0) or (tablero[f][c] != None)):
                continue
            elif not hay_adyacencias(f, c, tablero):
                filas_disponibles.append(f)
        demanda = demanda_columnas[c]
        nuevos_candidatos = posiciones_para_barco_por_columna(filas_disponibles, c, barco_size, todos)
        guardar_nuevos_candidatos(demanda, posiciones_candidatas, nuevos_candidatos)
        if not todos and len(nuevos_candidatos) > 0:
            return list(posiciones_candidatas.items())

    return list(posiciones_candidatas.items())

def puedo_poner(tablero, demanda_filas, demanda_columnas, barco_size):
    alternativas = obtener_candidatos(tablero, demanda_filas, demanda_columnas, barco_size, False)
    if len(alternativas) == 0:
        return False
    demanda, alternativa = alternativas[0]
    return len(alternativa[0]) > 0

'''
    Pos: Basandose en el estado actual del tablero y las demandas, y teniendo en cuenta
         solamente a los barcos de la lista que se encuentran entre los indices
         [i+1, final_idx] y caben en el tablero, se retorna el valor de la demanda total
         que podria satisfacerse si pudieramos colocarlos a todos ellos.
'''
def demanda_proyectada(tablero, demanda_filas, demanda_columnas, barcos, i):
    demandas = []
    for j in range(i + 1, len(barcos)):
        barco_idx, barco_size = barcos[j]
        if puedo_poner(tablero, demanda_filas, demanda_columnas, barco_size):
            demandas.append(barco_size*2)
    return sum(demandas)

'''
    Pre: barcos es una lista de tuplas de la forma (barco_id, barco_size) ordenada de
         manera descendente según el valor "barco_size".

    Pos: Sea barcos[i] el barco actual, devuelve un indice de la lista en el cual haya
         otro barco con un "barco_size" distinto al barco actual.
'''
def obtener_siguiente_distinto(barcos, i):
    actual = barcos[i]
    actual_idx, actual_size = actual
    for j in range(i + 1, len(barcos)):
        siguiente_idx, siguiente_size = barcos[j]
        if siguiente_size != actual_size:
            return j
    return i + 1
