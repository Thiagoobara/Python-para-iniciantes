'''
Faça um programa que leia três números e mostre qual o maior e qual o menor.
'''


num1 = float(input('Digite o 1° número '))
num2 = float(input('Digite o 2° número '))
num3 = float(input('Digite o 3° número '))
num_max = max(num1, num2, num3)
num_min = min(num1, num2, num3)
print('O número maior entre {:.1f}, {:.1f} e {:.1f} é {:.1f}'.format(num1, num2, num3, num_max))
print('E o de menor valor é {:.1f}'.format(num_min))
print('-----FIM------')
