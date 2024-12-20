﻿# TP1 grupal de TDA
## Instrucciones para correr el sistema

### Correr el sistema
Para correr el sistema ejecute el main.
```bash
...\TP-TDA\TP1> python3 main.py
```

Una vez ejecutado el main se mostrara un menu con las siguientes opciones:

![imagen](https://github.com/user-attachments/assets/4d26aa32-48d4-4368-8ea8-15febca643c7)

### 1. Correr a partir de la ruta completa de un archivo
Para correr el programa a partir de la ruta de un archivo, ingrese 1. La salida estará en `/out/output.txt`

### 2. Correr los test proporcionados por la catedra
Para correr los test ingrese 2. Por consola se imprimirá si la prueba fue exitosa, con la ganancia correspondiente.

### 3. Correr los test creados por el grupo
Para correr los test ingrese 3. Por consola se imprimirá si la prueba fue exitosa, con la ganancia correspondiente.

### 4. Correr los test creados por mí
Para correr los test creados por usted, ingrese 4. Estos tests deben crearse en el directorio `/tests/user_tests` según el formato detallado más abajo.

### 5. Correr el gráfico de datos
Para correr el gráfico de datos ingrese 5. Luego, se abrirá una ventana con el gráfico.

#### Requisitos de los archivos de test

El sistema leerá todos los archivos `.txt` que se encuentran en los directorios de pruebas. Estos archivos deben cumplir con los siguientes formatos:

1. Los archivos con los test deben ser `.txt` y comenzar con un número (ejemplo: `1.txt`)
2. Deben contener el set de numeros de la siguiente forma: w;x;y;...;z, en una sola linea y separados por ';'.
3. Cualquier otra linea que no sea la que contenga dichos valores debe comenzar con '#'.

Al ejecutarse con los datos leídos, el sistema comparará la salida con el archivo `Resultados Esperados.txt`. Este archivo debe cumplir con el siguiente formato:

1. Debe comenzar con el nombre del archivo a comparar.
2. En la siguiente línea debe tener la salida esperada del programa contando cuál pieza toma cada jugador.
3. Finalmente, en la última línea debe tener la ganancia siguiendo el formato `Ganancia de Sophia: {ganancia}`
4. Cualquier otra linea que no sea la que contenga dichos valores debe comenzar con '#'.
