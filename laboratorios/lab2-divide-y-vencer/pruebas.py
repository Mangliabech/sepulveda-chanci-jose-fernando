"""Pruebas del subarreglo maximo: casos fijos y comparacion con fuerza bruta."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo, suma_cruzada


def ejecutar_pruebas() -> None:
    """Ejecuta todas las pruebas; lanza AssertionError si alguna falla."""
    # 1. Serie de 8 dias del enunciado
    serie_enunciado = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie_enunciado)[2] == 17
    assert subarreglo_maximo(serie_enunciado, 0, len(serie_enunciado) - 1)[2] == 17

    # 2. Serie de un solo elemento
    un_elemento = [-5]
    assert subarreglo_fuerza_bruta(un_elemento)[2] == -5
    assert subarreglo_maximo(un_elemento, 0, 0)[2] == -5

    # 3. Serie con todos los valores negativos
    todos_negativos = [-10, -3, -8, -1, -5]
    assert subarreglo_fuerza_bruta(todos_negativos)[2] == -1
    assert subarreglo_maximo(todos_negativos, 0, len(todos_negativos) - 1)[2] == -1

    # 4. Serie con todos los valores positivos (el tramo es toda la serie)
    todos_positivos = [1, 4, 2, 10, 3]
    assert subarreglo_fuerza_bruta(todos_positivos)[2] == 20
    assert subarreglo_maximo(todos_positivos, 0, len(todos_positivos) - 1)[2] == 20

    # 5. Caso donde el mejor tramo cruza obligatoriamente el punto medio.
    # medio = (0 + 5) // 2 = 2, asi que la mitad izquierda es indices 0..2 y
    # la derecha 3..5. Mejor tramo izquierdo: [8] = 8 (o [2, -1, 8] = 9);
    # mejor tramo derecho: [12] = 12. El mejor tramo global es
    # [2, -1, 8, 12] = 2 - 1 + 8 + 12 = 21, indices 0..3, que cruza el medio.
    tramo_cruzado = [2, -1, 8, 12, -4, 3]
    ultimo = len(tramo_cruzado) - 1
    inicio_tc, fin_tc, suma_tc = subarreglo_maximo(tramo_cruzado, 0, ultimo)
    assert (inicio_tc, fin_tc, suma_tc) == (0, 3, 21)
    assert subarreglo_fuerza_bruta(tramo_cruzado) == (0, 3, 21)
    # La funcion auxiliar tambien debe devolver el tramo cruzado
    assert suma_cruzada(tramo_cruzado, 0, 2, ultimo) == (0, 3, 21)

    # 6. La funcion no debe modificar la lista de entrada
    copia = list(tramo_cruzado)
    subarreglo_maximo(tramo_cruzado, 0, ultimo)
    subarreglo_fuerza_bruta(tramo_cruzado)
    assert tramo_cruzado == copia

    # 7. Al menos 20 listas aleatorias comparando ambas soluciones
    random.seed(42)
    for _ in range(30):
        tamanio = random.randint(1, 100)
        lista_aleatoria = [random.uniform(-100.0, 100.0) for _ in range(tamanio)]

        res_fb = subarreglo_fuerza_bruta(lista_aleatoria)[2]
        res_dv = subarreglo_maximo(lista_aleatoria, 0, len(lista_aleatoria) - 1)[2]

        # Comparacion con tolerancia por punto flotante
        assert abs(res_fb - res_dv) < 1e-7, (
            f"Discrepancia encontrada: FB={res_fb}, DV={res_dv}"
        )

    print("Todas las pruebas pasaron exitosamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
