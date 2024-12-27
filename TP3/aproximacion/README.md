# Resolución Batalla Naval por aproximación
## Instrucciones para correr el sistema

### Correr el sistema
Para correr el sistema ejecute el main indicando el path de la carpeta con los test a correr:

```bash
...\TP-TDA\TP3\aproximacion> python main.py path
```

### Correr los test proporcionados por la catedra
```bash
...\TP-TDA\TP3\aproximacion> python main.py ../tests/given_tests
```

### Correr los test creados por el grupo
```bash
...\TP-TDA\TP3\aproximacion> python main.py ../tests/group_tests
```

#### Requisitos de los archivos de test

El sistema tiene la capacidad de ejecutar más de un test a la vez, por lo que para la ruta absoluta se espera que sea un directorio, NO un archivo. Luego el sistema leerá todos los archivos `.txt` que se encuentran en el directorio. Estos archivos deben cumplir con los siguientes formatos: 

1. Los archivos con los test deben ser `.txt`
2. Se espera recibir tres sets.
3. El primer set debe corresponder a las demandas de las filas.
4. El segundo set debe corresponder a las demandas de las columnas.
5. El tercer set debe corresponder a laslongitudes de los barcos.
6. Los sets se deben separar con una linea vacia.
7. Cada elemento del set debe escribirse en una linea distinta. Cada linea debe contener como maximo un numero.
8. Cualquier otra linea que no sea la que contenga dichos valores debe comenzar con '#'.

Ejemplo:
```bash
3
1
2

3
2
0

1
1
```
### Resultado de los test
El resultado de este test se encuentra en el directorio out/ dentro del proyecto.
Para guardar estos resultados cambiarle el nombre al archivo de salida.
De lo contrario se sobreescribira.