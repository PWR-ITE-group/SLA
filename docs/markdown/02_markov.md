## Lańcuch Markowa w czasie ciągłym (CTMC - Continuous Time Markov Chain)

Łańcuch Markowa w czasie ciągłym to rodzaj łancucha Markowa w którym **stany zmieniają się w spoób ciągły w czasie**.

CTMS jest 4-elementową krotką $(S,\Lambda, Q, \theta)$
<!-- ![przykład ](./images/markov.png) -->
<figure>
  <img
  src="./images/markov.png"
  alt="CTMC"
  style="width: 80%;"
  >
  <figcaption>Przykład Łańcuchu Markowa w czasie ciągłym</figcaption>
</figure>

### Zbiór stanów $S$
$S$ jest skończonym zbiorem stanów 
$S = \{S_1, S_2,\dots, S_{n-1}, S_n\}$

W powyższym przykładzie
$S = \{S_1, S_2, S_3, S_4\}$

### Macierz intensywności

Macierz intensywności $Q$ jest macierzą $n \times n$ gdzie $n$ to liczba stanów w modelu. Opisuje ona przejścia między stanami, jej elementy to parametry intensywności $\lambda_{ij}$.

$T_{i}$ -  średni czas bycia w stanie $i$

$$\lambda_{ij} = \frac{1}{T_{i}}$$


Dla modelu możemy zdefiniować macierz przejść. 
$$Q = [q_{ij}]$$

$$q_{ij} = \begin{cases}
\lambda_{ij} & \text{dla } i \neq j \\
-\sum_{k=1, k \neq i}^{n} \lambda_{ik} & \text{dla } i = j
\end{cases}$$

<figure>
  <img
  src="./images/q-matrix.png"
  alt="CTMC"
  style="width: 80%;"
  >
  <figcaption>Macierz Q dla przykładu</figcaption>
</figure>

Możemy zauważyć, że suma każdego wiersza jest równa $0$.

### Zbiór wartości i funkcja wartości

$A$ - skończony zbiór wartości, które mogą być przypisane do stanów.

$\Theta : S \mapsto  A$ - funkcja wartości, która przypisuje wartość z $A$ do każdego stanu $S_i$.


### Rozkład stacjonarny

W przypadku proces Markowa, rozkład stacjonarny opisuje prawdopodobieństwo przebywania w danym stanie, kiedy czas $t$ dąży do nieskończoności. Sposoby obliczenia prawdopoobieństwa przebywania w danym stanie opiszemy dwoma sposobami:

#### Metoda pierwsza
$\pi$ - wektor prawdopodobieństw stacjonarnych. Np. $\pi = [\pi_1, \pi_2, \dots, \pi_n]$ i $\pi_i$ to prawdopodobieństwo przebywania w stanie $i$.

$$\pi Q = 0$$

$$\sum_{i \in S} \pi_i = 1$$

#### Metoda druga
$A_{prob}$ - powstaje z macierzy $Q$ poprzez zamianę ostatniej kolumny na wektor złożony z jedynek.

$$\pi = [0,0,\dots,0,1]_{1\times n} A_{prob}^{-1}$$


##### Linki
- https://dl.acm.org/doi/pdf/10.1145/343369.343402