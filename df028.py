'''
Escreva um programa que faça o computador 'pensar' em um número inteiro 0 a 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo pc.
'''
import random
import time 
# sempre deixar atrativo para o cliente
print('-=-' * 20)
num = int(input('Advinhe o número que pensei, ele fica entre 0 a 5. '))
print('-=-' * 20)
print('Estou pensando......')
time.sleep(2)
print('Ainda estou pensando.....')
ale = random.randint(0, 5)
if num == ale :
    time.sleep(2)
    print('Parabéns o número era {}'.format(ale))
else:
    time.sleep(2)
    print('Errou o número que pensei era {}'.format(ale))



