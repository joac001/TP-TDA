'''
    Pos: Devuelve True si algun casillero a radio 1 de distancia de la
         la posicion (f, c) esta siendo ocupado por otro barco en el tablero.
'''
def hay_adyacencias(f, c, tablero):
    filas = len(tablero)
    columnas = len(tablero[0]) if filas > 0 else 0
    radio = 1

    for i in range(max(0, f - radio), min(filas, f + radio + 1)):
        for j in range(max(0, c - radio), min(columnas, c + radio + 1)):
            if tablero[i][j] is not None:
                return True 
    return False

def colocar_barco(casilleros, tablero, barco):
    for casillero in casilleros:
        i, j = casillero
        tablero[i][j] = barco

def actualizar_demandas(casilleros, demanda_filas, demanda_columnas, incremento):
    for casillero in casilleros:
        demanda_unitaria = -1 if incremento else 1
        f, c = casillero
        demanda_filas[f] -= demanda_unitaria
        demanda_columnas[c] -= demanda_unitaria