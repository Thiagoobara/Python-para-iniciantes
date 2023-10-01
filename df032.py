'''
Faça um programa que mostre se o ano é bissexto
'''
ano = int(input('Digite o ano '))
bi = ano % 4
if bi == 0:
    print('Esse ano é bissexto ')
else:
    print('Esse ano não é bissexto ')
print('---FIM---')
