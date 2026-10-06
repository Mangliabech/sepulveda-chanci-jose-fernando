# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Jose Fernando Sepúlveda Chanci · **Laboratorio:** Plataforma Tamiza — ordenamiento, complejidad y recurrencias
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `0f8af41`

Muy buen trabajo: el informe es claro, el código funciona y sus conclusiones se apoyan en mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 18 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **84 / 100** |
| **Nota (0–5)** | **4.20** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue a tiempo, y nombra la ventana de 4 horas como la restricción que se incumple.
- Explica con números (60 veces más datos, 3.600 veces más trabajo) por qué duplicar el servidor no resuelve el problema.
- Da dos perjuicios concretos (el paciente y el operador del centro de contacto) y dice quién asume el costo de cada uno.

**Lo que puede mejorar:**
- En la parte ambiental falta una cifra o un cálculo aproximado de energía; "cientos de kWh" se afirma sin mostrar de dónde sale.
- El segundo ejemplo (búsqueda de talentos) es válido, pero sería más sólido si dijera claramente qué sistema fue y cómo conoció esos datos.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y promedio indicando sobre qué se toma cada uno, justifica usar el peor caso y deja escrita la predicción antes del experimento.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando la condición.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- El análisis línea a línea de insertion sort queda a medias: pone las cantidades de ejecuciones, pero no suma los costos ni llega a la expresión final del peor y el mejor caso.
- Para el peor y el mejor caso conviene explicar qué forma tiene la lista de entrada, no solo el escenario.

## 3. Corrección de la implementación (18 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no alteran la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`.
- Los tres generadores dan listas de valores distintos, del tamaño pedido, y los aleatorios son reproducibles con semilla.

**Lo que puede mejorar:**
- La función interna de `merge_sort` no tiene explicación (docstring).

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas tienen título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica correctamente el peor caso (orden inverso), el mejor (casi ordenado) y el promedio (aleatorio), y contrasta con su predicción.
- El concepto técnico recomienda merge sort, rechaza el servidor con un dato medido, extrapola a 1.200.000 registros y lo declara como estimación.

**Lo que puede mejorar:**
- Algunos números del informe no coinciden con las gráficas publicadas: por ejemplo, la gráfica de la Parte 4 muestra cerca de 2,8 segundos para insertion sort con 6.400 registros y el texto dice 2,06; en la Parte 3 el texto dice 6,7 segundos para el orden inverso y la gráfica muestra cerca de 5,7. Las estimaciones de 4.3 se apoyan en esos números.
- Se explica poco lo que ocurre con tamaños pequeños; solo se menciona el costo de la recursión de forma general.
- No indica si repitió las mediciones o las hizo una sola vez, lo que explica parte de la variación.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- Carpeta y archivos en la ubicación y con los nombres acordados; gráficas incrustadas con ruta que sí funciona; enlaces a los `.py`; informe ordenado por partes; seis commits descriptivos sobre el laboratorio.

**Lo que puede mejorar:**
- El informe no trae su nombre completo.
- Las instrucciones de reproducción no explican cómo activar el entorno virtual del curso.
- Los enlaces al código están agrupados al inicio; cada parte práctica debía enlazar su código al comienzo de la Parte 3 y de la Parte 4.

## ¿El código funciona?
Sí. Los scripts corren sin errores, ordenan correctamente y generan las tres gráficas en pocos segundos.

## Para el próximo laboratorio
- Copie los números del informe directamente de la última ejecución, para que texto y gráficas coincidan.
- Complete los cálculos paso a paso hasta el resultado final, incluso los que parecen obvios.
- Incluya su nombre completo y todos los pasos de reproducción, activando el entorno virtual.
- Enlace el código al inicio de cada parte práctica y repita las mediciones varias veces, indicándolo en el informe.
- Agregue docstring a las funciones internas.
