'''
Desenvolva um programa que leia o comprimento de 3 retas e diga se ela pode ou não formar um triangulo.
'''
r1 = float(input('Digite a 1° reta '))
r2 = float(input('Digite a 2° reta '))
r3 = float(input('Digite a 3° reta '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Sim, é possível formar um triangulo. ')
else:
    print('Não é possível formar um triangulo ')
print('---Fim----')