'''
Faça um programa que leia uma frase pelo teclado e mostre
quantas vezes aparece a letra 'A'
em que posição ela aparece a 1° 
em que posição ela aparece a ultima vez  
'''

frase = str(input('Digite uma frase ')).lower().strip()
print("A letra A aparece {} vezes".format(frase.count('a')))
print('A letra A aparece a 1° vez na posição {}'.format(frase.find('a')+1))
print("A letra A aparece a uma vez na posição {}".format(frase.rfind('a')+1))

