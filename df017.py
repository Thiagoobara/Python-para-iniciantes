'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
'''
# c2=a2+b2.
from math import pow
ct = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))
r = pow(ct) + (ca)
print('Comprimento da hipotenusa séra de {}'.format(r))

