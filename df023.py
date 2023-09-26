'''
Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um numero : 1834

unidades : 4
dezena : 3
centena : 8
milhar : 1
'''
#// divisão inteira
#% resto da divisão
nu = int(input('Digite um número de 0 a 9999 '))
uni = nu // 1 % 10
de = nu // 10 % 10
cent = nu // 100 % 10
mil = nu // 1000 % 10
print('Valor em uni {}'.format(uni))
print('Valor da dez {}'.format(de))
print('Valor da cent {}'.format(cent))
print('Valor de mil {}'.format(mil))

