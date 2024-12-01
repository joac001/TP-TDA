# Imports necesarios para el notebook
from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from util import time_algorithm
from monedas import monedas

# Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme()

def cuadrados_minimos(x, t):
    f = lambda x, c1, c2: c1 * x + c2

    c, pcov = sp.optimize.curve_fit(f, x, [t[n] for n in x])

    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x + c[1] - [t[n] for n in x])**2)
    print(f"Error cuadrático total: {r}")

    return c

def graficar_datos(x, t, c):
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [t[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución del algoritmo')
    ax.set_xlabel("Cantidad de monedas")
    ax.set_ylabel('Tiempo de ejecución (s)')

    ax.plot(x, [c[0] * n + c[1] for n in x], 'r--', label="Ajuste")
    ax.legend()

def graficar_error(x, t, c):
    ax: plt.Axes
    fig, ax = plt.subplots()
    errors = [np.abs(c[0] * n + c[1] - t[n]) for n in x]
    ax.plot(x, errors)
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Error absoluto (s)')

def correr_grafico():
    x = (10, 100, 1000, 10000, 100000, 1000000) # Cantidad de monedas
    t = time_algorithm(monedas, x, lambda s: [np.random.randint(1, 999, size=s).tolist(), [], []])
    c = cuadrados_minimos(np.array(x), t)

    graficar_datos(x, t, c)
    #graficar_error(x, t, c)

    plt.show()
