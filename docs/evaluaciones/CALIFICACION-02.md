# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Jose Fernando Sepulveda · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `5e07184`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 17 / 25 |
| Calidad del análisis de las gráficas | 14 / 25 |
| Documentación y organización del informe | 3 / 10 |
| **Total** | **67 / 100** |
| **Nota (0–5)** | **3.35** |

## 1. Corrección conceptual (15 / 20)
**Lo que hizo bien:**
- Compara con el máximo de un arreglo y explica que dividir no mejora (`T(n) = 2T(n/2) + Θ(1)` da `Θ(n)`).
- Recomienda divide y vencerás y da una estimación a 1.000.000 de registros sin usar regla de tres lineal.

**Lo que puede mejorar:**
- La estimación y la conclusión sobre tamaños pequeños usan tiempos que no coinciden con su gráfica publicada (ver punto 4), así que los 16 horas y 2.91 segundos no están bien respaldados.
- Dice que divide y vencerás gana desde n = 50, pero no lo sustenta con valores de su gráfica; además dice "milisegundos" para tamaños donde los tiempos son mucho menores.
- Falta decir con claridad que el resultado es una estimación y qué la puede alterar.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea la recurrencia, explica de dónde sale cada término y aplica el caso 2 del método maestro comparando `f(n)` con `n^(log_b a)`.
- Justifica el `Θ(n²)` de la fuerza bruta contando los pares de días.

**Lo que puede mejorar:**
- Falta resolver la recurrencia paso a paso o mostrar por qué el caso cruzado cuesta exactamente un recorrido lineal.

## 3. Corrección de la implementación (17 / 25)
**Lo que hizo bien:**
- Las tres funciones están bien: dan la suma correcta, resuelven los tres casos, no llaman a la fuerza bruta y no modifican la lista. Coinciden en cientos de listas aleatorias.
- Tienen *type hints* y *docstrings*.

**Lo que puede mejorar:**
- `pruebas.py` falla al ejecutarse: en el caso del tramo cruzado espera 20, pero la respuesta correcta es 21 (2 − 1 + 8 + 12). El error está en la prueba, no en el algoritmo, pero así las pruebas no terminan con éxito.
- `medicion.py` y `pruebas.py` no tienen la *docstring* de módulo y la función de pruebas no tiene tipo de retorno.

## 4. Calidad del análisis de las gráficas (14 / 25)
**Lo que hizo bien:**
- La gráfica existe, con las dos curvas en los mismos ejes, título, ejes rotulados y leyenda, y cubre ocho tamaños (de 10 a 8000) con semilla fija.
- Calcula el factor al duplicar n para ambos algoritmos y lo compara con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Los valores del informe no coinciden con la gráfica publicada: el informe dice que fuerza bruta pasa de 0.92 s a 3.71 s (n = 4000 a 8000), pero en `tiempo_vs_n.png` pasa de cerca de 2.85 s a cerca de 4.13 s, un factor de unos 1.45 y no 4. Lo mismo ocurre con divide y vencerás (cerca de 0.03 s en n = 8000, no 0.0152 s).
- La gráfica publicada no parece corresponder a una sola corrida limpia (el salto entre 2000 y 4000 es muy grande); conviene repetir cada medición y usar el promedio o la mediana, y decirlo en el informe.

## 5. Documentación y organización del informe (3 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab2-divide-y-vencer/` está en una ubicación válida y tiene todos los archivos pedidos.
- Hay más de tres commits con mensajes descriptivos.

**Lo que puede mejorar:**
- El informe no tiene su nombre ni las instrucciones para reproducir (activar entorno, ejecutar pruebas y medición).
- No sigue el orden pedido: faltan las secciones de la Parte 1 y la Parte 2.
- No enlaza `subarreglo.py`, `pruebas.py` ni `medicion.py`.
- La gráfica no está incrustada en el informe: solo se menciona su nombre, así que no se ve en GitHub.

## ¿El código funciona?
Los algoritmos funcionan y dan resultados correctos. `medicion.py` corre y genera la gráfica, pero `pruebas.py` se detiene con un error por un valor esperado mal calculado en una prueba.

## Para el próximo laboratorio
- Ejecute siempre sus pruebas antes de entregar y revise a mano los valores esperados.
- Copie en el informe los números que lee de su propia gráfica publicada y haga los cálculos con ellos.
- Siga el orden del entregable: nombre, instrucciones, Parte 1, Parte 2 con la gráfica incrustada, Parte 3, con enlaces al código.
- Repita las mediciones y use el promedio o la mediana para evitar saltos por ruido.
- Agregue docstrings de módulo, type hints (incluido el tipo de retorno) y dos líneas en blanco entre funciones en todos los archivos.
