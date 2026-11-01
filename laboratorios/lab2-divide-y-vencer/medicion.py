"""Medicion de tiempos: fuerza bruta vs. divide y venceras."""

import os
import random
import statistics
import time
from collections.abc import Callable

import matplotlib

matplotlib.use("Agg")  # Backend sin ventana: funciona sin pantalla
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

SEMILLA = 42
TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 7  # cada medicion se repite y se reporta la mediana


def medir(funcion: Callable[[], object], repeticiones: int = REPETICIONES) -> float:
    """Mide el tiempo de una llamada y devuelve la mediana de varias corridas.

    Args:
        funcion: funcion sin argumentos que ejecuta el algoritmo a medir.
        repeticiones: cuantas veces se repite la medicion.

    Returns:
        La mediana de los tiempos, en segundos.
    """
    tiempos: list[float] = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def ejecutar_experimento() -> tuple[list[int], list[float], list[float]]:
    """Ejecuta el experimento de tiempo de ejecucion para ambos algoritmos.

    Returns:
        Tupla con las listas de tamanos, tiempos de fuerza bruta y tiempos
        de divide y venceras (mediana de varias repeticiones, en segundos).
    """
    random.seed(SEMILLA)  # Semilla fija para reproducibilidad

    tiempos_fb: list[float] = []
    tiempos_dv: list[float] = []

    print(f"Mediana de {REPETICIONES} repeticiones por tamano (semilla {SEMILLA}).")
    print(f"{'N':>6} | {'Suma coincide':>13} | {'Tiempo FB (s)':>15} | {'Tiempo DV (s)':>15}")
    print("-" * 58)

    for n in TAMANOS:
        # Generar datos fuera del cronometro
        datos = [float(random.randint(-100, 100)) for _ in range(n)]

        tiempo_fb = medir(lambda: subarreglo_fuerza_bruta(datos))
        tiempo_dv = medir(lambda: subarreglo_maximo(datos, 0, n - 1))

        # Verificacion de coincidencia de las sumas
        res_fb = subarreglo_fuerza_bruta(datos)
        res_dv = subarreglo_maximo(datos, 0, n - 1)
        coinciden = abs(res_fb[2] - res_dv[2]) < 1e-7
        assert coinciden, f"Discrepancia en N={n}: FB={res_fb[2]}, DV={res_dv[2]}"

        tiempos_fb.append(tiempo_fb)
        tiempos_dv.append(tiempo_dv)

        print(f"{n:6d} | {str(coinciden):>13} | {tiempo_fb:15.6f} | {tiempo_dv:15.6f}")

    return TAMANOS, tiempos_fb, tiempos_dv


def generar_grafica(
    tamanos: list[int], tiempos_fb: list[float], tiempos_dv: list[float]
) -> None:
    """Genera y guarda la grafica comparativa de tiempos de ejecucion."""
    os.makedirs("graficas", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(
        tamanos,
        tiempos_fb,
        marker="o",
        linewidth=2,
        color="crimson",
        label=r"Fuerza bruta $\Theta(n^2)$",
    )
    plt.plot(
        tamanos,
        tiempos_dv,
        marker="s",
        linewidth=2,
        color="royalblue",
        label=r"Divide y vencerás $\Theta(n \log n)$",
    )

    plt.title("Tiempo de ejecución: fuerza bruta vs. divide y vencerás", fontsize=14)
    plt.xlabel("Tamaño de entrada $n$ (número de días)", fontsize=12)
    plt.ylabel(f"Tiempo de ejecución (s), mediana de {REPETICIONES} corridas", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=11)
    plt.tight_layout()

    ruta_grafica = os.path.join("graficas", "tiempo_vs_n.png")
    plt.savefig(ruta_grafica, dpi=150)
    plt.close()
    print(f"\nGráfica guardada en '{ruta_grafica}'.")


if __name__ == "__main__":
    resultado = ejecutar_experimento()
    generar_grafica(*resultado)
