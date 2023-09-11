'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario com 15% de aumento. 
'''
sa = float(input('Digite seu salário atual R$'))
sr = sa + (sa * 15/100)
print('Parabéns seu salário que era de R${:.2f} com reajuste de 15% foi para R${:.2f}.'.format(sa , sr))
