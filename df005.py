'''
Operadores aritiméticos
+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% resto da divisão
Ordem de precedêmcia 
1° ()
2° **
3° * / // % 
4° + -
Obs raiz quadrada 81**(1/2)
                  25**(1/2)
Obs raiz cubica 127**(1/3)
                87**(1/3)
5 + 3 * 2 == 11
2°      1°   

3 * 5 + 4 ** 2 == 31
  2°  3°       1°

3 * (5 + 4) ** 2 == 243
  3°     1°    2° 
'''
n1 = int(input('Digite um valo! '))
n2 = int(input('Digite outro valor! '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e a potência {}'.format(di, e))

#obs para o resultado ficar com x casas decimais {:.3f}
# para print na msm linha ), end=' ') ex
'''
print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A Divisão inteira é, {}, e a potência {}'.format(di, e))
para quebra a linha \n ex: print('O valor de {}.\n e o valor de {}.'.format())
'''
