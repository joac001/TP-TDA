import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import time
import os
from max_coins import max_coins

def probar_max_coins(tamanos, num_pruebas=3):
    tiempos = []
    errores = []  # Lista para almacenar la desviación estándar
    for tamano in tamanos:
        tiempo_por_tamano = []
        for _ in range(num_pruebas):
            monedas = np.random.randint(10, 1001, size=tamano)
            tiempo_inicio = time.time()
            max_coins(monedas)
            tiempo_fin = time.time()
            tiempo_por_tamano.append(tiempo_fin - tiempo_inicio)
        tiempos.append(np.mean(tiempo_por_tamano))
        errores.append(np.std(tiempo_por_tamano))
    return tiempos, errores

def run_analysis():
    
    print("Corriendo analisis y generando graficos...")
    
    # Tamaños de prueba desde 10 hasta 1000 aumentando de a 10
    tamanos = list(range(10, 1001, 10))
    tiempos_ejecucion, errores = probar_max_coins(tamanos)

    # Regresión de mínimos cuadrados para ajuste cuadrático
    x = np.array(tamanos)
    y = np.array(tiempos_ejecucion)
    A = np.vstack([x**2, x, np.ones(len(x))]).T
    a, b, c = np.linalg.lstsq(A, y, rcond=None)[0]

    # Creación de subplots: uno para el análisis principal y otro para el error
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

    # Gráfica principal
    ax1.plot(tamanos, tiempos_ejecucion, 'bo-', label='Mediciones reales', alpha=0.5)
    teorica = [n*n * (tiempos_ejecucion[0] / (tamanos[0]**2)) for n in tamanos]
    ax1.plot(tamanos, teorica, 'r--', label='Teórica O(n²)')
    ax1.set_xlabel('Número de Monedas')
    ax1.set_ylabel('Tiempo de Ejecución (segundos)')
    ax1.set_title('Análisis de Complejidad Temporal de max_coins')
    ax1.grid(True)
    ax1.legend()

    # Gráfica de error
    ax2.plot(tamanos, errores, 'r-', label='Error (Desviación Estándar)')
    ax2.fill_between(tamanos, np.array(errores), alpha=0.2, color='red')
    ax2.set_xlabel('Número de Monedas')
    ax2.set_ylabel('Desviación Estándar')
    ax2.set_title('Análisis de Error en las Mediciones')
    ax2.grid(True)
    ax2.legend()
    
    tmp_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp", "complexity_analysis.png")
    

    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")):
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp"))

    plt.tight_layout()
    plt.savefig(tmp_file)
    plt.show()
    print(f"Analisis completo. Imagen guardada en {tmp_file}")
