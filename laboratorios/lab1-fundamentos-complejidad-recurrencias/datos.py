"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random
from typing import List


def generar_aleatorio(n: int, semilla: int = 42) -> List[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: Cantidad de registros del lote.
        semilla: Semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n índices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    # Rango amplio para asegurar n valores únicos distintos
    limite_superior = max(1_000_000, n * 10)
    return rng.sample(range(0, limite_superior), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> List[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: Cantidad de registros del lote.
        semilla: Semilla del generador aleatorio.

    Returns:
        Lista de n índices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce (descendente) y el 2%
        restante desordenado al final.
    """
    rng = random.Random(semilla)
    limite_superior = max(1_000_000, n * 10)
    valores = rng.sample(range(0, limite_superior), n)

    n_98 = int(n * 0.98)

    # Ordenamiento descendente manual de los primeros n_98 elementos (sin sort/sorted)
    parte_98: List[int] = []
    for x in valores[:n_98]:
        inserted = False
        for idx in range(len(parte_98)):
            if x > parte_98[idx]:
                parte_98.insert(idx, x)
                inserted = True
                break
        if not inserted:
            parte_98.append(x)

    parte_restante = valores[n_98:]
    return parte_98 + parte_restante


def generar_inverso(n: int) -> List[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: Cantidad de registros del lote.

    Returns:
        Lista de n índices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir (ascendente).
    """
    # El algoritmo produce orden descendente (mayor a menor).
    # El orden inverso es estrictamente ascendente (menor a mayor).
    return list(range(1, n + 1))