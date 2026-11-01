"""Experimentos A y B: lista frente a tabla hash, y efecto del factor de carga."""
import random
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

SEMILLA = 42
BUSQUEDAS = 200
REPETICIONES = 3
ESTADOS = ["en bodega", "en reparto", "entregado"]
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(k: int) -> bool:
    """Indica si k es primo.

    Args:
        k: entero a evaluar.

    Returns:
        True si k es primo.
    """
    if k < 2:
        return False
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False
        i += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Devuelve el primo mas cercano (hacia arriba) a un objetivo.

    Args:
        objetivo: valor de referencia.

    Returns:
        El menor primo mayor o igual a objetivo.
    """
    k = max(2, objetivo)
    while not es_primo(k):
        k += 1
    return k


def generar_guias(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador.

    Returns:
        Lista de n enteros distintos de diez digitos.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def construir(guias: list[int], m: int) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista y la tabla con las mismas guias.

    Args:
        guias: guias a insertar.
        m: casillas de la tabla.

    Returns:
        La lista y la tabla ya pobladas.
    """
    azar = random.Random(SEMILLA)
    lista, tabla = ListaEnlazada(), TablaHash(m)
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar(lista: ListaEnlazada, tabla: TablaHash, guias: list[int]) -> None:
    """Comprueba que lista y tabla coinciden en una muestra de guias existentes.

    Args:
        lista: lista poblada.
        tabla: tabla poblada.
        guias: guias existentes.
    """
    muestra = random.Random(SEMILLA).sample(guias, min(200, len(guias)))
    for guia in muestra:
        assert lista.buscar(guia) == tabla.buscar(guia) is not None


def tiempo_medio(estructura, consultas: list[int]) -> float:
    """Mide el tiempo medio por busqueda (mejor de varias repeticiones).

    Args:
        estructura: objeto con metodo buscar.
        consultas: guias a buscar.

    Returns:
        Segundos promedio por busqueda.
    """
    mejor = float("inf")
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in consultas:
            estructura.buscar(guia)
        mejor = min(mejor, time.perf_counter() - inicio)
    return mejor / len(consultas)


def experimento_a() -> list[tuple[int, int, float, float, float]]:
    """Ejecuta el experimento A y genera lista_vs_tabla.png.

    Returns:
        Filas (n, m, alfa, t_lista, t_tabla).
    """
    filas = []
    for n in (100, 500, 1000, 5000, 20000, 50000):
        guias = generar_guias(n)
        m = primo_cercano(n // 2)
        lista, tabla = construir(guias, m)
        verificar(lista, tabla, guias)
        consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS)
        t_lista = tiempo_medio(lista, consultas)
        t_tabla = tiempo_medio(tabla, consultas)
        filas.append((n, m, tabla.factor_carga(), t_lista, t_tabla))
        print(f"A n={n} m={m} alfa={tabla.factor_carga():.2f} "
              f"lista={t_lista*1e6:.3f}us tabla={t_tabla*1e6:.3f}us")
    ns = [f[0] for f in filas]
    plt.figure(figsize=(7, 4.5))
    plt.plot(ns, [f[3] * 1e6 for f in filas], "o-", label="Lista enlazada")
    plt.plot(ns, [f[4] * 1e6 for f in filas], "s-", label="Tabla hash (alfa ~ 2)")
    plt.title("Busqueda de guias inexistentes: lista vs tabla hash")
    plt.xlabel("Numero de guias n (unidades)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()
    return filas


def experimento_b() -> list[tuple[float, int, float]]:
    """Ejecuta el experimento B y genera tiempo_vs_alfa.png.

    Returns:
        Filas (alfa_objetivo, m, t_tabla).
    """
    n = 20000
    guias = generar_guias(n)
    consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS)
    filas = []
    for alfa in (0.25, 0.5, 1, 2, 4, 10):
        m = primo_cercano(round(n / alfa))
        _, tabla = construir(guias, m)
        t = tiempo_medio(tabla, consultas)
        filas.append((tabla.factor_carga(), m, t))
        print(f"B alfa={tabla.factor_carga():.2f} m={m} tabla={t*1e6:.3f}us")
    plt.figure(figsize=(7, 4.5))
    plt.plot([f[0] for f in filas], [f[2] * 1e6 for f in filas], "o-",
             label="Tabla hash, n = 20.000")
    plt.title("Tiempo de busqueda frente al factor de carga")
    plt.xlabel("Factor de carga alfa = n / m (adimensional)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()
    return filas


if __name__ == "__main__":
    experimento_a()
    experimento_b()