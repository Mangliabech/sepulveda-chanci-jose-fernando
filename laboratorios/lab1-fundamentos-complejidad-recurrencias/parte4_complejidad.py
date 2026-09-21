"""Experimento de la Parte 4: Comparación de tiempo de ejecución entre algoritmos."""

import os
import time
from typing import List
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def ejecutar_experimento_complejidad() -> None:
    """Ejecuta el experimento comparativo de la Parte 4 sobre el Escenario A.

    Mide el tiempo de ejecución de Insertion Sort y Merge Sort para siete
    tamaños de entrada sobre lotes aleatorios (Escenario A) usando
    time.perf_counter(). Genera la gráfica parte4_tiempo.png en 'graficas/'.
    """
    os.makedirs("graficas", exist_ok=True)

    tamanos: List[int] = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_insertion: List[float] = []
    tiempos_merge: List[float] = []

    for n in tamanos:
        # Generar datos desordenados (Escenario A)
        data = generar_aleatorio(n, semilla=42)

        # Medir tiempo de Insertion Sort (cronometrando únicamente el algoritmo)
        t0 = time.perf_counter()
        _, _ = insertion_sort(data)
        t1 = time.perf_counter()
        tiempos_insertion.append(t1 - t0)

        # Medir tiempo de Merge Sort (cronometrando únicamente el algoritmo)
        t0 = time.perf_counter()
        _, _ = merge_sort(data)
        t1 = time.perf_counter()
        tiempos_merge.append(t1 - t0)

    # Generar gráfica comparativa: Tiempo vs. Tamaño de Entrada
    plt.figure(figsize=(8, 6))
    plt.plot(
        tamanos,
        tiempos_insertion,
        "o-",
        color="crimson",
        label="Insertion Sort",
    )
    plt.plot(tamanos, tiempos_merge, "s-", color="navy", label="Merge Sort")

    plt.title("Comparación de Tiempo de Ejecución en Escenario A (Aleatorio)")
    plt.xlabel("Tamaño de entrada N (cantidad de registros)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar_experimento_complejidad()