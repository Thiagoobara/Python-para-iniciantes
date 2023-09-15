'''
Faça um programa que leia um angulo qualquer na tela o valor do seno, cosseno e tangente desse ângulo
'''

from math import sin, radians, cos, tan
an = float(input('Digite o ângulo: '))
se = sin(radians(an))
co = cos(radians(an))
tg = tan(radians(an))
print('O ângulo de {}°\nTem o seno de {:.2f}\nSeu cosseno é de {:.2f}\nE sua tangente {:.2f}'.format(an, se, co, tg))

