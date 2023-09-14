'''
Crie um programa  que leia um número  real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex:
Digite um numero :6.127
O numero 6.127 tem a parte inteira 6.
'''

import math
n = float(input('Digite um numero '))
r = math.trunc(n)
print('A porção inteira de {} séra de {}. '.format(n, r))


