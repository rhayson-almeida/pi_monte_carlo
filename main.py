# Programa para calcular o valor de pi com o método Monte Carlo.
import numpy as np
from math import sqrt

if __name__ == '__main__':
    mcs = int(input('Insira o número de passos de Monte Carlo: '))
    mp =  int(input('Insira o número de pontos para a média: '))
    sum1 = sum2 = pimed = erropi = 0
    for i in range(mp):
        y = 0   
        for j in range(mcs):
            x = np.random.random()
            y += sqrt(1-x**2)

        pi = 4*(y/mcs)
        sum1 += pi
        sum2 += pi**2
    
    pimed = sum1/mp
    erro  = sqrt((sum2 - (sum1**2)/mp)/(mp*(mp-1)))
    print(f'o valor de pi é {pimed} +/- {erro}')