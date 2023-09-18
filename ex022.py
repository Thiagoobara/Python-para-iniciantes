'''
Manipulando texto.
fatiamento
frase = print('Curso em Video Python')
01234567891011121314151617181920

ex: print(frase[9]) ele identifica o caracter de n°10 que seria (V)
ex2: print(frase[9:13]) ele pegaria da letra V ate o E pois ele conta sempre uma casa antes no final.
ex3: print(frase[9:13:2]) ele ira ate o 12 pulando de 2 e 2 caracter
ex4:  print(frase[:13]) ele vai entender como 0 e print(frase[5:]) a logica reversa .
ex5: print(frase[9::3])ele ira do 9 em diante pulando de 3 em 3

Análise
len(frase) OBS: len vem do ingles comprimento 
frase.count('o') OBS: você esta pedindo para o programa contar quandos o vão aparecer (letra miniscula)
frase.count('o',0,13) contagem com fatiamento







'''
frase =('Curso em Video Python')
print(frase[9])
frase =('Curso em Video Python')
print(frase[9:13])
frase =('Curso em Video Python')
print(frase[9:21:2])
frase =('Curso em Video Python')
print(frase[:5])
frase =('Curso em Video Python')
print(frase[5:])
frase =('Curso em Video Python')
print(frase[9::3])
frase =('Curso em Video Python')
print(len(frase))
frase =('Curso em Video Python')
print(frase.count('o'))
frase =('Curso em Video Python')
print(frase.count('o',0,13))