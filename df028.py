'''
Escreva um programa que faça o computador 'pensar' em um número inteiro 0 a 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo pc.
'''
import random
num = int(input('Digite um numero de 0 a 5 '))
ale = random.randint(0, 5)
if num == ale :
    print('Parabéns ')
else:
    print('Errou')


