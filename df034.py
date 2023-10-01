'''
Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento 
para maiores de R$1.250.00 um aumento de 10% para inferiores  aumento de 15%
'''
sal = float(input('Digite seu salario '))
aumento_menor = sal + (sal * 10 / 100)
aumento_maior = sal + (sal * 15 / 100)
if sal >= 1250:
    print('Seu salario ajustado será de R${:.2f}'.format(aumento_menor))
else:
    print('Seu salario ajustado será de R${:.2f}'.format(aumento_maior))

print('---Fim---')