'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
km = int(input('Valor em km percorridos '))
al = float(input('Dias alugados '))
ap = (0.15 * km )+ (al * 60)
print('Valor a ser pago R${:.2f}.'.format(ap))
