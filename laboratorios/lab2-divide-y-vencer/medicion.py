import os
import random
import time
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_experimento() -> tuple[list[int], list[float], list[float]]:
    """Ejecuta el experimento de tiempo de ejecucion para ambos algoritmos.

    Returns:
        Tupla con las listas de tamanos, tiempos de fuerza bruta y tiempos
        de divide y venceras.
    """
    # Semilla fija para reproducibilidad
    random.seed(42)

    # Tamanos requeridos (incluye <100 y >=4000)
    tamanos = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
    tiempos_fb: list[float] = []
    tiempos_dv: list[float] = []

    print(f"{'N':>6} | {'Suma Coincide':>13} | {'Tiempo FB (s)':>15} | {'Tiempo DV (s)':>15}")
    print("-" * 58)

    for n in tamanos:
        # Generar datos fuera del cronometro
        datos = [float(random.randint(-100, 100)) for _ in range(n)]

        # Cronometrar Fuerza Bruta
        inicio_fb = time.perf_counter()
        res_fb = subarreglo_fuerza_bruta(datos)
        fin_fb = time.perf_counter()
        tiempo_fb = fin_fb - inicio_fb

        # Cronometrar Divide y Venceras
        inicio_dv = time.perf_counter()
        res_dv = subarreglo_maximo(datos, 0, n - 1)
        fin_dv = time.perf_counter()
        tiempo_dv = fin_dv - inicio_dv

        # Verificacion de coincidencia exacta de sumas
        coinciden = abs(res_fb[2] - res_dv[2]) < 1e-7
        assert coinciden, f"Discrepancia en N={n}: FB={res_fb[2]}, DV={res_dv[2]}"

        tiempos_fb.append(tiempo_fb)
        tiempos_dv.append(tiempo_dv)

        print(f"{n:6d} | {str(coinciden):>13} | {tiempo_fb:15.6f} | {tiempo_dv:15.6f}")

    return tamanos, tiempos_fb, tiempos_dv


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
        label="Fuerza Bruta $\Theta(n^2)$",
    )
    plt.plot(
        tamanos,
        tiempos_dv,
        marker="s",
        linewidth=2,
        color="royalblue",
        label="Divide y Venceras $\Theta(n \log n)$",
    )

    plt.title("Tiempo de Ejecución: Fuerza Bruta vs. Divide y Vencerás", fontsize=14)
    plt.xlabel("Tamaño de Entrada $n$ (Número de Días / Registros)", fontsize=12)
    plt.ylabel("Tiempo de Ejecución (segundos)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=11)
    plt.tight_layout()

    ruta_grafica = os.path.join("graficas", "tiempo_vs_n.png")
    plt.savefig(ruta_grafica, dpi=300)
    plt.close()
    print(f"\nGráfica guardada exitosamente en '{ruta_grafica}'.")


if __name__ == "__main__":
    tamanos, tiempos_fb, tiempos_dv = ejecutar_experimento()
    generar_grafica(tamanos, tiempos_fb, tiempos_dv)