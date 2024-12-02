from common.test_reader import read_test_case

VERTICAL = 'V'
HORIZONTAL = "H"

#Verifica que la pocision dada y sus posiciones adyacentes esten vacias
def posicion_vacia (i , j , tablero):
    for dx, dy in [(0, 0), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                
        adyacente_x = i + dx
        adyacente_y = j + dy

        if ( (0 <= adyacente_x < len(tablero)) and (0 <= adyacente_y < len(tablero[0])) and (tablero[adyacente_x][adyacente_y] != 0) ):
            return False
    
    return True

# Valida si se puede ubicar un barco en la posicion y direccion recibidas, respetando los limites del tablero, cumpliendos las restricciones del mismo y evitando adyacencias con otros barcos

def se_puede_ubicar(i, j, longitud, direccion , tablero, demandas_filas , demandas_columnas):

    if (direccion == HORIZONTAL) :
        
        # Verificamos que el barco no se sale del tablero
        if ( (j + longitud) > len(tablero[0]) ):  
            return False

        # Verificamos que los casilleros a ocupar estén libres, no tengan barcos adyacentes y cumplan las demandas de las columnas
        for col in range(j, (j + longitud)):            
            if ((not posicion_vacia(i , col , tablero)) or (demandas_columnas[col] < 1)):
                return False 
    
    else:
    
        # Verificamos que el barco no se sale del tablero
        if ((i + longitud) > len(tablero)): 
            return False
        
        # Verificamos que los casilleros a ocupar estén libres, no tengan barcos adyacentes y cumplan las demandas de las filas
        for fila in range(i, i + longitud):          
            if ((not posicion_vacia(fila , j , tablero)) or (demandas_filas[fila] < 1)):
                return False
    
    return True


# Ubica un barco en el tablero y actualiza las demandas de filas y columnas.

def ubicar_barco(i, j, longitud, direccion , tablero , demandas_filas , demandas_columnas):
    if (direccion == HORIZONTAL):
        for col in range(j, j + longitud):
            tablero[i][col] = 1
            demandas_filas[i] -= 1
            demandas_columnas[col] -= 1
    else:
        for fila in range(i, i + longitud):
            tablero[fila][j] = 1
            demandas_filas[fila] -= 1
            demandas_columnas[j] -= 1


def batalla_naval_greedy(demandas_filas, demandas_columnas, barcos):

    demanda_cumplida = 0
    demanda_total = sum(demandas_filas) + sum(demandas_columnas)
    tablero = [[0]*len(demandas_columnas) for _ in range(len(demandas_filas))]
    
    # Ordenamos los barcos de mayor a menor longitud
    barcos.sort(reverse=True)   
    

    # Intentamos ubicar cada barco en todos los casilleros del tablero y  en ambos sentidos

    for barco in barcos:
        colocado = False
        
        for fila in range(len(tablero)):
            for col in range(len(tablero[0])):
               
                if ((demandas_filas[fila] >= barco) and (demandas_columnas[col] >= 1) and (se_puede_ubicar(fila, col, barco, HORIZONTAL, tablero, demandas_filas , demandas_columnas))):
                        ubicar_barco(fila, col, barco, HORIZONTAL, tablero, demandas_filas, demandas_columnas)
                        colocado = True
                        break 
                elif ((demandas_filas[fila] >= 1) and (demandas_columnas[col] >= barco) and (se_puede_ubicar(fila, col, barco, VERTICAL, tablero, demandas_filas , demandas_columnas))):
                        ubicar_barco(fila, col, barco, VERTICAL, tablero, demandas_filas, demandas_columnas)
                        colocado = True
                        break
           
            if colocado:
                break
    

    demanda_incumplida = sum(demandas_filas) + sum(demandas_columnas)
    demanda_cumplida = demanda_total - demanda_incumplida
    
    return tablero , demanda_total, demanda_cumplida , demanda_incumplida 
