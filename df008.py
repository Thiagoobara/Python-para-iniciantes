'''
Faça um programa que leia o valor em metros e converta em cm e mili
vkm = vm / 1000
vhm = vm / 100
vda = vm / 10
vdm = vm * 10
vcm = vm * 100
vmm = vm * 1000
'''
vm = float(input('Digite um valor em metros '))
print('Valor em km {}.\nValor em hecto {}\nValor em deca {}\nValor em deci {}\nValor em cm {}\nValor em mm{}.'.format((vm/1000), (vm/100), (vm/10), (vm*10), (vm*100), (vm*1000)))
