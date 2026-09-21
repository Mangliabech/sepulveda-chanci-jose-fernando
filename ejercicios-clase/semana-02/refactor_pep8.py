from typing import List


def calcular_promedio(numeros: List[float]) -> float:
    """Calcula el promedio aritmético de una lista de números.

    Args:
        numeros (List[float]): Lista de números enteros o flotantes.

    Returns:
        float: El promedio aritmético de los números en la lista.
    """
    suma_total: float = 0.0
    for numero in numeros:
        suma_total += numero
    return suma_total / len(numeros)


def main() -> None:
    lista_numeros: List[float] = [1.0, 2.0, 3.0, 4.0, 5.0]
    promedio: float = calcular_promedio(lista_numeros)
    print(f"El promedio es: {promedio}")


if __name__ == "__main__":
    main()