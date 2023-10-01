'''
Desenvolva um programa que pergunte a distância de uma viagem em km calcule o preço da passagem cobrando R$0.50 por km para viagens até 200 km e R$0.45 para viagens maiores 
'''
kmp = float(input('Quantos km percorreu? '))
km200 = kmp * 0.50
kmf = kmp * 0.45
if kmp <= 200:
    print('Sua passagem ficara em R${:.2f}'.format(km200))
else:
    print('Sua passagem ficara em R${:.2f}'.format(kmf))
print('---MUITO OBRIGADO---')

    