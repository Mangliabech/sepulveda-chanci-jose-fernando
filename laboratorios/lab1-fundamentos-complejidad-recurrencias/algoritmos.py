"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""

from typing import List, Tuple


def insertion_sort(datos: List[int]) -> Tuple[List[int], int]:
    """Ordena una lista de índices de riesgo con el método de inserción.

    No modifica la lista recibida: trabaja sobre una copia. El ordenamiento
    se realiza en orden descendente (de mayor a menor) para priorizar los
    índices de riesgo más altos.

    Args:
        datos: Lista de índices de riesgo enteros a ordenar.

    Returns:
        Una tupla donde el primer elemento es la lista ordenada de mayor a
        menor y el segundo es el número total de comparaciones realizadas
        entre elementos de la lista.
    """
    arr = datos.copy()
    comparaciones = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key

    return arr, comparaciones


def merge_sort(datos: List[int]) -> Tuple[List[int], int]:
    """Ordena una lista de índices de riesgo con el método de mezcla.

    No modifica la lista recibida: trabaja sobre una copia. Implementa una
    estrategia de divide y vencerás para ordenar en orden descendente
    (de mayor a menor).

    Args:
        datos: Lista de índices de riesgo enteros a ordenar.

    Returns:
        Una tupla donde el primer elemento es la lista ordenada de mayor a
        menor y el segundo es el número total de comparaciones realizadas
        entre elementos de la lista durante el proceso de mezcla.
    """
    arr = datos.copy()

    def _merge_sort_rec(sub_arr: List[int]) -> Tuple[List[int], int]:
        if len(sub_arr) <= 1:
            return sub_arr, 0

        medio = len(sub_arr) // 2
        izq, comp_izq = _merge_sort_rec(sub_arr[:medio])
        der, comp_der = _merge_sort_rec(sub_arr[medio:])

        mezclado = []
        i = j = 0
        comp_mezcla = 0

        # Mezcla para mantener orden descendente (mayor a menor)
        while i < len(izq) and j < len(der):
            comp_mezcla += 1
            if izq[i] >= der[j]:
                mezclado.append(izq[i])
                i += 1
            else:
                mezclado.append(der[j])
                j += 1

        mezclado.extend(izq[i:])
        mezclado.extend(der[j:])

        total_comparaciones = comp_izq + comp_der + comp_mezcla
        return mezclado, total_comparaciones

    return _merge_sort_rec(arr)