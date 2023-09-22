'''
Crie um programa que leia o nome completo de uma pessoa e mostre
O nome com todas as letras maiúsculas
O nome com todas as letras minuscula
Quantas letras ao todo sem considerar espaço
Quantas letras tem o 1° nome
'''
nome = input(' Digite seu nome completo ')
print(nome.upper())
print(nome.lower())
n2 = len(nome.replace(" " ,"" ))
print(n2)


