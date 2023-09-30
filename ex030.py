'''
Média 
'''
n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
me = (n1 + n2) / 2
print('Sua média foi de {}'.format(me))
print('Passou' if me >= 5 else 'Não passou')

'''
    print('Sua média foi de {:.2f} passou'.format(me))
else:
    print('Sua média foi de {:.2f} não passou'.format(me))
'''

