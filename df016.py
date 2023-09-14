'''
Módulos
ex: matc Matemática 
matc
ceil = aredonda p cima
floor = aredonda p baixo
trunc = alimina da , para frente  
pow = potência
sqrt = raiz quadrada
factorial = fatorial

ex
import math vai importar toda a math
import math sqrt
'''
'''
Exemplo 1
import math
n = float(input('Digite um numero '))
r = math.sqrt(n)
print('Raiz quadrada é de {}'.format(math.ceil (r)))
'''
'''
Exemplo 2 importando 1
from math import sqrt
n = float(input('Digite um numero '))
r = sqrt(n)
print('Raiz quadrada é de {:.2f}'.format(r))
'''
'''
Exemplo 2 importando 2
from math import sqrt , floor
n = float(input('Digite um numero '))
r = sqrt(n)
print('Raiz quadrada é de {:.2f}'.format((floor(r))))
'''
''''
Exemplo 3 random e randint
import random
nu = random.randint(1, 10 )
print(nu)
'''

'''
import random
nu = random.randint(1, 10 )
print(nu)
'''
'''
import emoji
print( 'Olá, Mundo :\U0001f596', use_aliases=True'))
'''
import emoji

print(emoji.emojize(":grinning_face_with_big_eyes:"))
print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))
print(emoji.emojize("Python é :rosto_risonho:", language='pt'))

                    

