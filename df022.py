'''
Crie um programa que leia o nome completo de uma pessoa e mostre
O nome com todas as letras maiúsculas
O nome com todas as letras minuscula
Quantas letras ao todo sem considerar espaço
Quantas letras tem o 1° nome
'''
nome = str(input(' Digite seu nome completo ')).strip()
print('Seu nome em letras maiusculas será: {}'.format(nome.upper()))
print('Seu nome em letras minusculas será: {}'.format(nome.lower()))
print('A quantidade de Letras é de {}'.format(len(nome)-nome.count(' ')))     
print('Seu primeiro nome é composto por {} letras.'.format(nome.find(' ')))


