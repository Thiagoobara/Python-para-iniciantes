'''
Crie um programa que leia um numero inteiro e fale se ele e par ou impar
'''

num = int(input('Digite um numero '))
par = num % 2 
if par == 0:
    print('O número que escolheu é Par {}'.format(num))
else:
    print('O número que escolheu é Ímpar {}'.format(num) )
