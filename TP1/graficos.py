# Imports necesarios para el notebook
from random import seed

from matplotlib import pyplot as plt
#import seaborn as sns
import numpy as np
import scipy as sp
import os

from util import time_algorithm
from monedas import monedas

# Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
seed(12345)
np.random.seed(12345)

#sns.set_theme()

def cuadrados_minimos(x, t):
    f = lambda x, c1, c2: c1 * x + c2

    c, pcov = sp.optimize.curve_fit(f, x, [t[n] for n in x])

    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x + c[1] - [t[n] for n in x])**2)
    print(f"Error cuadrático total: {r}")

    return c

def graficar_datos(x, t, c, file):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

    # Gráfico de tiempo de ejecución
    ax1.plot(x, [t[i] for i in x], label="Medición")
    ax1.plot(x, [c[0] * n + c[1] for n in x], 'r--', label="Ajuste")
    ax1.set_title('Tiempo de ejecución del algoritmo')
    ax1.set_xlabel("Cantidad de monedas")
    ax1.set_ylabel('Tiempo de ejecución (s)')
    ax1.legend()
    ax1.grid()

    # Gráfico de error
    errors = [np.abs(c[0] * n + c[1] - t[n]) for n in x]
    ax2.plot(x, errors)
    ax2.set_title('Error de ajuste')
    ax2.set_xlabel('Tamaño del array')
    ax2.set_ylabel('Error absoluto (s)')
    ax2.grid()

    plt.tight_layout()
    plt.savefig(file)
    plt.show()

def run_analysis():
    print("Corriendo analisis y generando graficos...")
    #x = (10, 100, 1000, 10000, 50000, 100000) # Cantidad de monedas
    x = np.linspace(10, 100000, 50, dtype=int)  # Cantidad de monedas con más puntos de prueba

    t = time_algorithm(monedas, x, lambda s: [np.random.randint(1, 999, size=s).tolist(), [], []])
    c = cuadrados_minimos(np.array(x), t)
    tmp_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp", "complexity_analysis.png")

    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")):
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp"))

    graficar_datos(x, t, c, tmp_file)
    print(f"Analisis completo. Imagen guardada en {tmp_file}")
