'''
Faça um programa que leia o nome completo de uma pessoa, mostrando apenas o 1° e o ultimo nome
'''

nome = str(input("Digite seu nome completo ")).upper().strip().split()
print("Primeiro nome {}".format(nome[0]))
print("Seu ultimo é {}". format(nome[len(nome)-1]))
