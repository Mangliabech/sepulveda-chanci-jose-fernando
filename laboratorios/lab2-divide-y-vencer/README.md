# Análisis del Problema del Subarreglo Máximo

## 1. Recurrencia y Complejidades Teóricas

El algoritmo de divide y vencerás divide el problema original de tamaño $n$ en **2 subproblemas** independientes sobre subarreglos de tamaño $n/2$ (mitades izquierda y derecha). La fase de combinación requiere calcular el subarreglo cruzado mediante dos barridos lineales que inician en el punto medio, sumando un costo temporal $\Theta(n)$.

La relación de recurrencia queda expresada como:
$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

Aplicando el **Método Maestro** de la forma $T(n) = aT(n/b) + f(n)$:
- $a = 2$ (dos llamadas recursivas).
- $b = 2$ (el tamaño del arreglo se divide a la mitad).
- $f(n) = \Theta(n)$ (costo lineal del caso cruzado).

Calculamos $n^{\log_b a} = n^{\log_2 2} = n^1 = n$. Al comparar $f(n) = \Theta(n)$ con $n^{\log_b a} = \Theta(n)$, observamos que coinciden asintóticamente. Por lo tanto, aplica el **Caso 2 del Método Maestro**, concluyendo que la complejidad total del algoritmo es:
$$T(n) = \Theta(n \log n)$$

Por otro lado, la **fuerza bruta** evalúa todos los subintervalos inclusivos $[i, j]$ con $0 \le i \le j < n$. Al acumular la suma iterativamente dentro del ciclo interno, se realizan $\sum_{i=0}^{n-1} (n - i) = \frac{n(n+1)}{2}$ iteraciones. Como cada paso ejecuta operaciones de suma y comparación en tiempo constante $O(1)$, la complejidad total es proporcional al número de pares, resultando en $\Theta(n^2)$.

---

## 2. Lo Medido contra lo Esperado

En la gráfica generada (`graficas/tiempo_vs_n.png`), la curva de **fuerza bruta** exhibe una parábola creciente que se dispara aceleradamente conforme aumenta $n$. En contraste, la curva de **divide y vencerás** mantiene una trayectoria casi lineal e inferior a lo largo de todo el dominio.

Tomando los tamaños consecutivos $n_1 = 4000$ y $n_2 = 8000$ ($n$ se duplica):
- **Fuerza Bruta:** El tiempo pasa de $0.92\text{ s}$ a $3.71\text{ s}$. El factor de incremento empírico es $\approx 4.03$, lo cual coincide con la predicción teórica de $\Theta(n^2)$, pues $(2n)^2 / n^2 = 4$.
- **Divide y Vencerás:** El tiempo pasa de $0.0071\text{ s}$ a $0.0152\text{ s}$. El incremento empírico es de $\approx 2.14$, ajustándose al factor teórico esperado:
  $$\frac{2n \log_2(2n)}{n \log_2(n)} = 2 \left(1 + \frac{1}{\log_2 n}\right) \approx 2.16 \quad \text{para } n = 4000$$

---

## 3. Comportamiento en Tamaños Pequeños

Para entradas pequeñas ($n = 10$ y $n = 50$), ambos algoritmos registran tiempos en el orden de milisegundos. Sin embargo, divide y vencerás supera a la fuerza bruta desde $n \ge 50$.

Aunque conceptualmente la fuerza bruta tiene menor sobrecosto de overhead en $n$ sumamente pequeños (al no crear marcos en la pila de llamadas ni calcular puntos medios), la implementación de fuerza bruta optimizada realiza $\frac{n(n+1)}{2}$ iteraciones en Python. Con $n = 100$, fuerza bruta ejecuta $5.050$ operaciones frente a las $\approx 664$ operaciones recursivas. Por ello, el umbral de ventaja (*crossover point*) ocurre muy temprano.

---

## 4. ¿Cuándo Conviene Dividir?

No siempre conviene dividir un problema. Si analizamos la búsqueda del **elemento máximo** en un arreglo de $n$ números:
- **Enfoque Iterativo:** Recorre el arreglo una vez comparando elementos, con costo $\Theta(n)$.
- **Enfoque Divide y Vencerás:** Partir el arreglo en dos mitades requiere resolver $2T(n/2)$ y comparar los dos ganadores con costo $\Theta(1)$. Su recurrencia es $T(n) = 2T(n/2) + \Theta(1)$. Por el Caso 1 del Método Maestro ($n^{\log_2 2} = n$), la solución es $\Theta(n)$.

**Conclusión:** Dividir no mejoró la complejidad asintótica ($\Theta(n)$ en ambos). Dividir solo conviene cuando la combinación de subproblemas es significativamente más barata que explorar directamente el espacio global de soluciones, o cuando elimina la necesidad de evaluar combinaciones redundantes, como ocurre en la racha máxima.

---

## 5. Recomendación y Estimación para la Gerencia

Recomiendo a la cooperativa adoptar **Divide y Vencerás**. 

### Estimación para $1.000.000$ de registros:
- **Fuerza Bruta:** Con $t(n) \approx c_1 \cdot n^2$, usando $n = 8000$ ($t \approx 3.71\text{ s}$), tenemos $c_1 \approx 5.8 \times 10^{-8}$.  
  Para $n = 1.000.000$: $t \approx 5.8 \times 10^{-8} \cdot (10^6)^2 \approx 58.000\text{ segundos} \approx \mathbf{16.1\text{ horas}}$.
- **Divide y Vencerás:** Con $t(n) \approx c_2 \cdot n \log_2 n$, usando $n = 8000$ ($t \approx 0.0152\text{ s}$), tenemos $c_2 \approx 1.46 \times 10^{-7}$.  
  Para $n = 1.000.000$ ($\log_2(10^6) \approx 19.93$): $t \approx 1.46 \times 10^{-7} \cdot 10^6 \cdot 19.93 \approx \mathbf{2.91\text{ segundos}}$.

Fuerza bruta tomaría **más de 16 horas** por tienda/sensor, mientras que divide y vencerás resolverá cada serie en **menos de 3 segundos**.