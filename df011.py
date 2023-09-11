'''
Calcule a area , e infome quanto de tinha sera necessario para pintar sabendo-se que 1 litro pinta 2m²
'''
vl = float(input('Digite a largura em metros '))
va = float(input('Digite a altura em metros '))
ar = vl * va
tn = ar / 2
print('Area é de {:.2f}m², e será necessario {:.2f} litros de tinta. '.format(ar, tn))