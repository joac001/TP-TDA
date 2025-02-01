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

Los archivos deben cumplir con los siguientes formatos:

Dados: x,y,...z el set de valores que representan a las monedas.

1. Los archivos con los test deben ser `.txt` 
2. Deben contener el set de numeros de la siguiente forma: w;x;y;...;z, en una sola linea y separados por ';'.
3. Cualquier otra linea que no sea la que contenga dichos valores debe comenzar con '#'.

### Hacer un analisis de complejidad
Para correr un analisis de complejidad ingrese la palabra 'analisis' en lugar del path. Se analizaran sets de 10 a 1000 monedas.

```bash
...\TP-TDA\TP1> python main.py analisis
```

### Resultado de los test
El resultado de este test se encuentra en el directorio out/ dentro del proyecto.
Para guardar estos resultados cambiarle el nombre al archivo de salida.
De lo contrario se sobreescribira.