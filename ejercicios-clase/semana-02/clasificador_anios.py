"""Clasificador de años bisiestos. Complete las funciones siguiendo la especificación de cada docstring."""


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio: año a evaluar (número entero).

    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).

    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada: str = input(
            "Ingrese una lista de años separados por comas (ej. 2024, 1900, 2000): "
        )
        try:
            # Dividimos la cadena por comas y convertimos cada valor a entero
            anios: list[int] = [int(item.strip()) for item in entrada.split(",") if item.strip()]
            
            if not anios:
                print("No ingresó ningún año válido. Intente de nuevo.\n")
                continue
                
            return anios
        except ValueError:
            print("Error: Asegúrese de ingresar únicamente números enteros separados por comas.\n")


def main() -> None:
    """Punto de entrada del script."""
    anios_ingresados: list[int] = leer_anios()

    # Comprensión de listas para filtrar únicamente los años bisiestos
    anios_bisiestos: list[int] = [anio for anio in anios_ingresados if es_bisiesto(anio)]

    # Impresión del resumen de resultados
    print("\n--- RESUMEN ---")
    print(f"Años ingresados: {anios_ingresados}")
    print(f"Años bisiestos encontrados: {anios_bisiestos}")
    print(f"Total de años bisiestos: {len(anios_bisiestos)} de {len(anios_ingresados)}")


if __name__ == "__main__":
    main()