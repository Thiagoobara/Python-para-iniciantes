'''
Escreva um programa que leia a velocidade de um carro .
se ele ultrapassar 80km , mostre a mensagem dizendo que ele foi multado 
a multa vai custar R$7,00 a cada km a cima 
'''
import time
vel = float(input('Digite a velocidade do carro '))
if vel >80:
    print('MULTADO!!!! Você excedeu a limite permitido')
    multa = (vel - 80) * 7
    time.sleep(1)
    print('Calculando o valor da multa aguarde ...')
    time.sleep(1)
    print('Sua multa foi de R${:.2f} diriga com responsabilidade! '.format(multa))
print('Boa viagem!!!! ')

    


    



