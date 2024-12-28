# Certificador de Batalla Naval
## Instrucciones para correr el sistema

### Correr el sistema
Para correr el sistema ejecute el main indicando el path de la carpeta  o archivo con los test a correr:

```bash
...\TP-TDA\TP3\certificador> python main.py path
```
Si se ingresa el path a una carpeta se correran todos los test en esa carpeta.

### Correr los test creados por el grupo
```bash
...\TP-TDA\TP3\certificador> python main.py ../tests/certificador_tests
```

#### Requisitos de los archivos de test

Los archivos deben cumplir con los siguientes formatos: 

1. Los archivos con los test deben ser `.txt`
2. Se espera recibir cuatro sets.
3. El primer set debe corresponder a las demandas de las filas.
4. El segundo set debe corresponder a las demandas de las columnas.
5. El tercer set debe corresponder a las longitudes de los barcos.
6. Cada elemento de los tres primeros sets debe escribirse en una línea distinta. Cada línea debe contener como máximo un número.
7. El cuarto set debe corresponder a la matriz del tablero. Las columnas deben estar separadas por un espacio y las columnas deben estar en distintas líneas. 
8. Los sets se deben separar con una linea vacia.
9. Cualquier otra linea que no sea la que contenga dichos valores debe comenzar con '#'.

Ejemplo:
```bash
0
1
1
1
0

0
0
2
0
1

1
1
1

0 0 0 0 0
0 0 1 0 0
0 0 0 0 1
0 0 1 0 0 
0 0 0 0 0 

```
### Resultado de los test
El resultado se mostrará en la terminal.
