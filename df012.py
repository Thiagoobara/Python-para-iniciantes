'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto.
'''
pa = float(input('Digite o valor do produto R$'))
pf = pa - (pa * 5 / 100)
print(' O produto que custava R${:.2f}, na promoção com 5% de desconto custara R${:.2f} .'.format(pa, pf))

      