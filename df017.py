'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
'''
# c2=a2+b2.
from math import pow, sqrt
ct = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))
r = pow(2.0,ct) + pow(2.0,ca)
c = sqrt(r)
print('Comprimento da hipotenusa séra de {:.2f}'.format(c))


