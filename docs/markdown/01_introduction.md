# Symulacja systemu naprawialnego

## Wstęp

Niniejszy dokument jest wstępną dokumentacją i planem działania.

1. Zaczynamy od opisu prostych symulacji z małą ilością parametrów wejściowych i wyjściowych. Następnie rozszerzamy symulacje o bardziej złożone modele, które wymagają większej ilości parametrów wejściowych i wyjściowych.

2. Tworzymy atrakcyjny model, który można dopasować do różnych przypadków.

## Koncepcje statystyczne

Przed opisem modelów, opiszemy kilka pojęć statystycznych

### Rozkład wykładnicza

Rozkład wykładniczy jest jednym z powszechnie używanych rozkładów ciągłych.
Obliczając gęstość funkcji wykładniczej od $0$ do $t$, możemy obliczyć prawdopodobieństwo pewnego zdarzenia.
Będziemy go używać w przejściach między stanami w modelach Markowa.

#### Funkcja gęstości prawdopodobieństwa

$$f(x) = \begin{cases}
\lambda e^{-\lambda x} & \text{dla } x \geq 0 \\
0 & \text{dla } x < 0
\end{cases}$$
#### Dystrybuanta

$$F(x) = \begin{cases}
1 - e^{-\lambda x} & \text{dla } x \geq 0 \\
0 & \text{dla } x < 0
\end{cases}$$

#### Wartość oczekiwana
Warto zauważyć, że wartość średnia jest równa odwrotności parametru $\lambda$.
$$E(X) = \frac{1}{\lambda}$$ 
Jest to o tyle ważne, że znając wartość średnią, możemy obliczyć parametr $\lambda$ rozkładu wykładniczego.
$$\lambda = \frac{1}{E(X)}$$


#### Przykład

Załóżmy, że średni czas przyjścia studenta do dziekanatu wynosi $10$ minut. Jakie jest prawdopodobieństwo, że student przyjdzie do dziekanatu w ciągu $15$ minut?
Z danych mamy, że $E(X) = 10$ minut. Zatem $\lambda = \frac{1}{10} = 0.1$.
Obliczamy prawdopodobieństwo, że student przyjdzie w ciągu $15$ minut.
$$P(X \leq 15) = 1 - e^{-0.1 \cdot 15} = 1 - e^{-1.5} \approx 0.7769$$

#### Własność braku pamięci

Rozkład wykładniczy ma własność braku pamięci. Oznacza to, że jeśli zdarzenie nie wystąpiło w ciągu pewnego czasu, to prawdopodobieństwo, że zdarzenie wystąpi w przyszłości, nie zależy od tego, jak długo zdarzenie nie wystąpiło.

$$P(X > s + t | X > s) = P(X > t)$$
