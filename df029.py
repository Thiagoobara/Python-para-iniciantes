'''
Escreva um programa que leia a velocidade de um carro .
se ele ultrapassar 80km , mostre a mensagem dizendo que ele foi multado 
a multa vai custar R$7,00 a cada km a cima 
'''

vel = float(input('Digite a velocidade do carro '))
limite = 80
multa = vel - limite
pag = multa * 7
if limite < 0:
    print('Não teve multa ')
else:
    print('Voce tera que pagar {:.2f} de multa pois estava a {:.2f} km por hora'.format(pag, vel ))




