"""Pruebas con assert para ListaEnlazada y TablaHash."""
import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ["en bodega", "en reparto", "entregado"]


def prueba_lista() -> None:
    lista = ListaEnlazada()
    lista.insertar(5, "entregado")
    lista.insertar(10, "en bodega")
    assert lista.tamano == 2
    assert lista.buscar(10) == "en bodega"
    assert lista.buscar(5) == "entregado"
    assert lista.buscar(99) is None  # busqueda infructuosa
    assert ListaEnlazada().buscar(1) is None  # lista vacia


def prueba_tabla() -> None:
    tabla = TablaHash(7)
    tabla.insertar(3, "en reparto")
    assert tabla.buscar(3) == "en reparto"
    assert tabla.buscar(4) is None  # casilla vacia
    assert tabla.buscar(10) is None  # misma casilla (3) pero no existe


def prueba_colision_forzada() -> None:
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        assert tabla.hash(guia) == 3
        tabla.insertar(guia, "en bodega")
    for guia in (10, 24, 17):
        assert tabla.buscar(guia) == "en bodega"
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7
    assert tabla.buscar(31) is None  # 31 % 7 == 3, no existe


def prueba_aleatorias() -> None:
    for semilla in range(25):
        azar = random.Random(semilla)
        n = azar.randint(0, 300)
        guias = azar.sample(range(10**9, 10**10), n)
        m = azar.choice([1, 7, 31, 101, 499])
        lista, tabla = ListaEnlazada(), TablaHash(m)
        for guia in guias:
            estado = azar.choice(ESTADOS)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
        existentes = set(guias)
        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia) is not None
        for _ in range(50):
            guia = azar.randint(10**9, 10**10 - 1)
            if guia not in existentes:
                assert lista.buscar(guia) is None
                assert tabla.buscar(guia) is None


if __name__ == "__main__":
    prueba_lista()
    prueba_tabla()
    prueba_colision_forzada()
    prueba_aleatorias()
    print("Todas las pruebas pasaron.")
