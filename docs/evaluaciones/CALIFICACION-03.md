# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Jose Fernando Sepulveda · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `2f34e6e`

Muy buen trabajo: la implementación es limpia y el análisis está bien razonado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 16 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **85 / 100** |
| **Nota (0–5)** | **4.25** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Explica bien la colisión y por qué ocurre aunque sobren casillas, y usa el ejemplo de las guías 10, 24 y 17 con m = 7 tanto en encadenamiento como en direccionamiento abierto.
- Justifica que la tabla hash no sirve para rangos y que el árbol sí.
- Estima la altura del árbol degenerado (400.000) frente al equilibrado (cerca de 19) y las comparaciones de cada caso.
- Recomienda una estructura que cubre las dos necesidades (consulta puntual y rango).

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación a 5.000.000 de envíos para la lista usa casi una regla de tres, y para la tabla y el árbol no da un tiempo concreto. Además no dice con claridad que sea una estimación.
  → *Cómo corregirlo:* declare expresamente "esto es una estimación", explique por qué la curva de cada estructura tiene esa forma y dé un tiempo aproximado para las tres, apoyado en un valor medido.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Justifica el Θ(n) de la lista y separa bien las dos partes del Θ(1 + α) de la tabla.
- Nombra el supuesto de hash uniforme y explica que, si todo cae en una casilla, la tabla se vuelve una lista.

**Lo que puede mejorar (y cómo corregirlo):**
- Para la lista dice que "recorre los n nodos" sin aclarar por qué se llega hasta el final cuando la guía no existe.
  → *Cómo corregirlo:* añada una frase que diga que solo se sabe que la guía no está después de ver todos los nodos.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` funcionan: búsquedas exitosas e infructuosas, colisión forzada con m = 7, `factor_carga` igual a 3/7.
- La tabla reutiliza la lista, sin `dict`, `set` ni `hash()`, y `buscar` usa un ciclo `while`.
- `pruebas.py` cubre todo lo pedido y compara lista y tabla en 25 colecciones aleatorias.
- Docstrings con `Args` y `Returns` y dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- En `medicion.py`, la función `tiempo_medio` no tiene *type hint* en el parámetro `estructura`.
  → *Cómo corregirlo:* indique el tipo, por ejemplo `estructura: ListaEnlazada | TablaHash`.

## 4. Calidad del análisis de las gráficas (16 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados y leyenda; la primera tiene seis valores de n con las dos curvas en los mismos ejes y la segunda seis valores de α.
- Mide solo las búsquedas con `time.perf_counter()`, usa semilla fija y verifica que lista y tabla coincidan.
- Compara con Θ(n), Θ(1) y Θ(1 + α) y reconoce el ruido de la medición.

**Lo que puede mejorar (y cómo corregirlo):**
- Las cifras del informe no coinciden con las gráficas publicadas. En `lista_vs_tabla.png` la lista llega a unos 7.400 µs con n = 50.000 y a unos 2.000 µs con n = 20.000; el informe dice 1.492 y 622. En `tiempo_vs_alfa.png` el tiempo con α = 10 es de cerca de 1,3 µs; el informe dice 0,634. Parece que las imágenes son de una corrida anterior a la que usó para escribir el texto.
  → *Cómo corregirlo:* ejecute `medicion.py` una última vez, suba los PNG nuevos y copie al informe los valores leídos de esas mismas imágenes.
- Los factores de crecimiento de la pregunta 2 salen de la tabla del informe, no de lo que se lee en las gráficas publicadas. Con las imágenes publicadas, de n = 5.000 a 20.000 la lista crece mucho menos de 4 veces y de 20.000 a 50.000 crece bastante más de 2,5; eso merecía una explicación.
  → *Cómo corregirlo:* lea dos valores consecutivos directamente de la gráfica, calcule el cociente y compárelo con lo que predice Θ(n); si no coincide, diga por qué.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- El `README.md` sigue el orden pedido, trae su nombre, enlaza el código de cada parte y las gráficas se incrustan con ruta relativa que sí existe.
- Hay cinco commits con mensajes descriptivos sobre el laboratorio.
- La carpeta `laboratorios/lab3-estructuras-datos/` es una ubicación válida.

**Lo que puede mejorar (y cómo corregirlo):**
- Las instrucciones de reproducción dicen `cd lab3-estructuras-datos`, pero el laboratorio está dentro de `laboratorios/`, así que ese comando falla desde la raíz.
  → *Cómo corregirlo:* cambie la ruta por `cd laboratorios/lab3-estructuras-datos`.

## ¿El código funciona?
Sí. Las pruebas pasan completas y `medicion.py` corre sin errores y genera las dos gráficas. La lista y la tabla devuelven los mismos resultados.
