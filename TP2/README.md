# TP2 grupal de TDA
## Instrucciones para correr el sistema

### Requisitos
Para instalar las dependencias para la generación de gráficos:
 ```bash
 pip install -r requirements.txt
 ```


### Correr el sistema
Para correrel sistema ejecute el main.
```bash
...\TP-TDA\TP2> python main.py
```

Una vez ejecutado el main se mostrara un menu con las siguientes opciones:

![menu](public/image.png)

### 2. Correr los test proporcionados por la catedra
Para correr los test ingrese 1. El resultado de los test se encuentra en `./out/output.txt`.

### 2. Correr los test creados por el grupo
Para correr los test ingrese 2. El resultado de los test se encuentra en `./out/output.txt`.

### 3. Correr los test creados por mí
Para correr los test creados por usted, ingrese 3. Luego, se le pedira una ruta absoluta al directorio donde se encuentran los test.

#### Requisitos de los archivos de test

El sistema tiene la capacidad de ejecutar más de un test a la vez, por lo que para la ruta absoluta se espera que sea un directorio, NO un archivo. Luego el sistema leerá todos los archivos `.txt` que se encuentran en el directorio. Estos archivos deben cumplir con los siguientes formatos: 

Dados: x,y,...z el set de valores que representan a las monedas.

1. los archivos con los test deben ser `.txt` 
2. Deben contener el set de numeros de la siguiente forma: w;x;y;...;z, en una sola linea y separados por ';'.
3. Cualquier otra linea que no sea la que contenga dichos valores debe comenzar con '#'.


#### ⚠️ IMPORTANTE: Cualquier otro archivo que no cumple con estos requisitos sera ignorado por el sistema.

### 4. Hacer un analisis de compljidad
Para correr un analisis de complejidad ingrese 4. Se analizara sets de 10 a 1000 monedas.