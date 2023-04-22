# Cálculo do valor de $\pi$ com o uso do método Monte Carlo.


O método Monte Carlo consiste em realizar uma caminhada aleatória de forma que pode ser utilizada para a integração de funções matemáticas. A rotina main.py define $\pi$ como

$$ \pi = 4 \times \left( \sum_i \sqrt{1-x_i^2}/N \right)$$

no qual $x$ é um número aleatório escolhido no intervalo entre $0$ e $1$.
