# Cálculo do valor de $\pi$ com o uso do método Monte Carlo.


O método Monte Carlo consiste em realizar uma caminhada aleatória de forma que pode ser utilizada para a integração de funções matemáticas. A rotina main.py define $\pi$ como

$$ \pi = \frac{4}{N} \times \left( \sum_{i=1}^N \sqrt{1-x_i^2}\right)$$

no qual $x_i$ são números aleatórios escolhidos no intervalo entre $0$ e $1$.
