'''
Um professor quer sortear um aluno para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
n1 = str(input('Digite o nome do(a) 1° aluno(a) '))
n2 = str(input('Digite o nome do(a) 2° aluno(a) '))
n3 = str(input('Digite o nome do(a) 3° aluno(a) '))
n4 = str(input('Digite o nome do(a) 4° aluno(a) '))
li = [n1, n2, n3, n4]
r = random.choice(li)
print('Entre os alunos {}, {}, {}, e {} o aluno sorteado foi {}'.format(n1, n2, n3, n4, r))

