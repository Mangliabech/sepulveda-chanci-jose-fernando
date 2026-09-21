"""Experimento de la Parte 3: Evaluación de casos para Insertion Sort."""

import os
import time
from typing import List
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def ejecutar_experimento_casos() -> None:
    """Ejecuta el experimento de la Parte 3 sobre los tres escenarios.

    Mide tiempo de ejecución y número de comparaciones de insertion_sort
    para siete tamaños de entrada en los escenarios A, B y C. Genera
    las gráficas comparativas en la carpeta 'graficas/'.
    """
    os.makedirs("graficas", exist_ok=True)

    tamanos: List[int] = [100, 200, 400, 800, 1600, 3200, 6400]

    res_a_comp: List[int] = []
    res_a_time: List[float] = []
    res_b_comp: List[int] = []
    res_b_time: List[float] = []
    res_c_comp: List[int] = []
    res_c_time: List[float] = []

    for n in tamanos:
        # Escenario A (Aleatorio)
        data_a = generar_aleatorio(n, semilla=42)
        t0 = time.perf_counter()
        _, comp_a = insertion_sort(data_a)
        t1 = time.perf_counter()
        res_a_comp.append(comp_a)
        res_a_time.append(t1 - t0)

        # Escenario B (Casi ordenado)
        data_b = generar_casi_ordenado(n, semilla=42)
        t0 = time.perf_counter()
        _, comp_b = insertion_sort(data_b)
        t1 = time.perf_counter()
        res_b_comp.append(comp_b)
        res_b_time.append(t1 - t0)

        # Escenario C (Orden inverso)
        data_c = generar_inverso(n)
        t0 = time.perf_counter()
        _, comp_c = insertion_sort(data_c)
        t1 = time.perf_counter()
        res_c_comp.append(comp_c)
        res_c_time.append(t1 - t0)

    # Gráfica 1: Comparaciones vs Tamaño de Entrada
    plt.figure(figsize=(8, 6))
    plt.plot(tamanos, res_a_comp, "o-", label="Escenario A (Aleatorio)")
    plt.plot(tamanos, res_b_comp, "s-", label="Escenario B (Casi ordenado)")
    plt.plot(tamanos, res_c_comp, "^-", label="Escenario C (Orden inverso)")
    plt.title("Comparaciones vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de entrada N (cantidad de registros)")
    plt.ylabel("Número de comparaciones entre elementos")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    # Gráfica 2: Tiempo de Ejecución vs Tamaño de Entrada
    plt.figure(figsize=(8, 6))
    plt.plot(tamanos, res_a_time, "o-", label="Escenario A (Aleatorio)")
    plt.plot(tamanos, res_b_time, "s-", label="Escenario B (Casi ordenado)")
    plt.plot(tamanos, res_c_time, "^-", label="Escenario C (Orden inverso)")
    plt.title("Tiempo de Ejecución vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de entrada N (cantidad de registros)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar_experimento_casos()