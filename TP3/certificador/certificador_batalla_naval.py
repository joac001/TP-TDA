def certificador_batalla_naval (tablero, barcos, restricciones_filas, restricciones_columnas):

    n = len(tablero)        
    m = len(tablero[0])     
    
    # 1 - Verificamos que las posiciones ocupadas por fila sean las correspondientes.

    for i in range(n):
        if ( sum(tablero[i]) != restricciones_filas[i] ):
            return False
    
    # 2 - Verificamos que las posiciones ocupadas por columna sean las correspondientes.

    for j in range(m):
        if ( sum(tablero[i][j] for i in range(n)) != restricciones_columnas[j] ):
            return False
    
    # Identificamos los barcos.

    visitados = [[False] * m for _ in range(n)]
    barcos_identificados = []

    def dfs(x, y, barco_actual):
        if ( not ( (0 <= x < n) and (0 <= y < m)) or visitados[x][y] or (tablero[x][y] == 0) ):
            return

        visitados[x][y] = True
        barco_actual.append((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(x + dx, y + dy, barco_actual)

    for i in range(n):
        for j in range(m):
            if ( (tablero[i][j] == 1) and not visitados[i][j] ):
                barco_actual = []
                dfs(i, j, barco_actual)
                barcos_identificados.append(barco_actual)
    

    # Identificamos los tamaños de los barcos encontrados
    
    tamaños_encontrados = []
    
    for barco in barcos_identificados:
    
        #3 - Verificamos que el ancho del barco es de un casillero
        
        filas = {x for x, y in barco}
        columnas = {y for x, y in barco}

        if ( (len(filas) > 1) and (len(columnas) > 1) ): 
            return False 
        
        tamaños_encontrados.append(len(barco))
        
        
        #4 - Verificamos que no haya adyacencia con otros barcos
        for x, y in barco:
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                
                adyacente_x = x + dx
                adyacente_y = y + dy

                if ( (0 <= adyacente_x < n) and (0 <= adyacente_y < m) and (tablero[adyacente_x][adyacente_y] == 1) ):
                    if (adyacente_x, adyacente_y) not in barco:
                        return False
    
    
    # 5 - Verificamos que los barcos identificados coincidan con los barcos dados

    if sorted(tamaños_encontrados) != sorted(barcos):
        return False
    
    return True

