def read_test_case(path):
    ''' 
    fields[0] -> Demanda por fila
    fields[1] -> Demanda por columna
    fields[2] -> Tamaño de cada barco
    '''
    fields = [], [], []
    field = None
    i = 0

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            
            if not line: # Linea vacia.
                i += 1
                continue
            
            if not line.isdigit():
                continue
            
            field = fields[i]
            field.append(int(line))
    
    return fields