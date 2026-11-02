# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Jose Fernando Sepulveda · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-11-02 23:59 · **Versión revisada:** commit `21e5da0`

Excelente trabajo: un informe muy completo, con datos propios y un código que funciona.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **94 / 100** |
| **Nota (0–5)** | **4.70** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica que el punto de cruce está entre n = 50 y n = 100 y lo explica con el costo de las llamadas recursivas en tamaños pequeños.
- Compara con el máximo de un arreglo: plantea `T(n) = 2T(n/2) + Θ(1)`, verifica el caso 1 del método maestro y concluye que dividir no mejora nada porque combinar es barato pero no hay nada que ahorrar.
- Recomienda divide y vencerás, estima 1.000.000 de registros (horas contra segundos), declara que es una estimación y explica qué puede alterarla.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación supone una constante fija calibrada con un solo tamaño, y no se discute cuánto cambia esa constante entre los tamaños medidos.
  → *Cómo corregirlo:* compare la constante obtenida con n = 4000 y con n = 8000 y comente si es estable antes de extrapolar.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Plantea la recurrencia explicando de dónde sale cada término (dos mitades, cruce lineal).
- Resuelve con el método maestro verificando la condición del caso 2 y además lo confirma con el árbol de recursión nivel por nivel.
- Justifica el `Θ(n²)` de la fuerza bruta contando las iteraciones, `n(n+1)/2`.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones devuelven la suma correcta en la serie de ocho días, un elemento, todos negativos, todos positivos y un caso cruzado.
- Ambos algoritmos coinciden en las listas aleatorias y ninguna modifica la lista recibida.
- `subarreglo_maximo` resuelve los tres casos y no llama a la fuerza bruta.
- Todas las funciones tienen *type hints* y *docstrings* con `Args` y `Returns`; hay dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- Las pruebas aleatorias usan números decimales, mientras que el experimento usa enteros entre -100 y 100.
  → *Cómo corregirlo:* agregue también listas aleatorias de enteros para probar el mismo tipo de datos que usa la medición.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con ocho tamaños (de 10 a 8000).
- Calcula el factor al duplicar n para cada algoritmo (fuerza bruta cerca de 4, divide y vencerás cerca de 2,09) y lo contrasta con lo esperado, con el valor teórico `n log n` calculado.
- Lo que afirma coincide con la gráfica: la fuerza bruta llega a cerca de 1 s en n = 8000 y la otra curva queda casi pegada al eje.

**Lo que puede mejorar (y cómo corregirlo):**
- En la gráfica los tamaños pequeños se amontonan al inicio del eje y el cruce entre 50 y 100 no se alcanza a ver; se apoya solo en la tabla.
  → *Cómo corregirlo:* agregue una segunda gráfica (o un recuadro) con solo los tamaños menores o igual a 500 y enlácela en el informe.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- La carpeta está en una ubicación válida (`laboratorios/lab2-divide-y-vencer/`) con todos los archivos pedidos.
- La gráfica se ve en el informe, el código está enlazado y hay instrucciones para reproducir.
- Hay más de tres commits con mensajes descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- No siguió el orden pedido del informe: la "Parte 1" del informe es la recurrencia, y falta la descripción de cómo verificó las soluciones y qué casos cubrió (ocho días, un elemento, negativos, positivos, cruzado, listas aleatorias).
  → *Cómo corregirlo:* agregue una Parte 1 con el enlace a `subarreglo.py` y `pruebas.py` y esa lista de casos; deje la Parte 2 para la gráfica con el enlace a `medicion.py` y la Parte 3 para las cinco respuestas.
- Las cinco preguntas del análisis no están numeradas ni separadas como en el enunciado (recurrencia, medido contra esperado, tamaños pequeños, cuándo dividir, concepto para la gerente), lo que hace difícil ubicarlas.
  → *Cómo corregirlo:* titule cada respuesta con el número y el nombre de la pregunta.
- La carpeta `graficas/` incluye un archivo `.gitkeep` que no era necesario.
  → *Cómo corregirlo:* elimínelo con `git rm laboratorios/lab2-divide-y-vencer/graficas/.gitkeep`.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan siempre la misma suma en listas aleatorias y el experimento está listo para regenerar la gráfica.
