# TP1 grupal de TDA
## Instrucciones para correr el sistema

### Requisitos
Para instalar las dependencias para la generación de gráficos:
 ```bash
 pip install -r requirements.txt
 ```

### Correr el sistema
Para correr el sistema ejecute el main indicando el path de la carpeta  o archivo con los test a correr:
```bash
...\TP-TDA\TP1> python main.py path
```
Si se ingresa el path a una carpeta se correran todos los test en esa carpeta.

### Correr los test proporcionados por la catedra

```bash
...\TP-TDA\TP1> python main.py tests/given_tests
```

### Correr los test creados por el grupo
```bash
...\TP-TDA\TP1> python main.py tests/group_tests
```

### Requisitos de los archivos de test

El sistema leerá todos los archivos `.txt` que se encuentran en los directorios de pruebas. Estos archivos deben cumplir con los siguientes formatos:

1. Los archivos con los test deben ser `.txt` y comenzar con un número (ejemplo: `1.txt`)
2. Deben contener el set de numeros de la siguiente forma: w;x;y;...;z, en una sola linea y separados por ';'.
3. Cualquier otra linea que no sea la que contenga dichos valores debe comenzar con '#'.

Al ejecutarse con los datos leídos, el sistema comparará la salida con el archivo `Resultados Esperados.txt`. Este archivo debe cumplir con el siguiente formato:

1. Debe comenzar con el nombre del archivo a comparar.
2. En la siguiente línea debe tener la salida esperada del programa contando cuál pieza toma cada jugador.
3. Finalmente, en la última línea debe tener la ganancia siguiendo el formato `Ganancia de Sophia: {ganancia}`
4. Cualquier otra linea que no sea la que contenga dichos valores debe comenzar con '#'.

### Hacer un analisis de compljidad
Para correr un analisis de complejidad ingrese la palabra 'analisis' en lugar del path. Se analizaran sets de 10 a 1000 monedas.

```bash
...\TP-TDA\TP1> python main.py analisis
```

### Resultado de los test
El resultado de este test se encuentra en el directorio out/ dentro del proyecto.
Para guardar estos resultados cambiarle el nombre al archivo de salida.
De lo contrario se sobreescribira.