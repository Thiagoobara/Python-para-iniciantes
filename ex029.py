'''
Crie um programa que pergunte o nome da pessoa e se for Luffy mostre reis dos piratas
'''

nome = str(input("Digite seu nome ")).strip().lower()
if nome == 'luffy':
    print("Rei dos piratas {}".format(nome))
else:
    print("{} não é um nome de REI".format(nome))
print("-----BOM DIA-----")