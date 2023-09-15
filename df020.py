'''
O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
a1 = str(input('Digite o nome do(a) 1° aluno(a) '))
a2 = str(input('Digite o nome do(a) 2° aluno(a)' ))
a3 = str(input('Digite o nome do(a) 3° aluno(a)' ))
a4 = str(input('Digite o nome do(a) 4° aluno(a) '))
lista = [a1, a2, a3, a4]

print('O primeiro aluno a se apresentar será {}.\nO segundo aluno a se apresentar será {}.\nO terceiro aluno a se apresentar será {}\nO quarto aluno a se apresentar será {}. ')