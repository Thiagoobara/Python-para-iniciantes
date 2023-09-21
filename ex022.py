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
find do ingles encotrar, então na frase ele procurara as letras que estra nas ''
'curso' in frase = ele procura a palavra na frase
frase.replace('Python', 'Android') do ingles trocar, ele vai achar a palavra Python e subistituira por Androide
frase.upper() para letras maiusculo 
frase.lower() para letras minuscula
frase.capitalize() joga todos os caracter em minuscula menos a primeira letra
frase.title() onde estiver espaço ele vai quebrar a palavra e tranformar a 1° letra em maiuscula
frase.strip() ele tira o espaço do começo e do fim da frase nunca do meio
frase.rstrip() ele tira o spaco do começo da frase porem so da direita
frase.lstrip() ele tira o spaco do começo da frase porem so da esquerda
frase.split() ocoore nos espaços, ele divide cada palvra e ms rece index novo faz um lista com cada palavra
'-'.join(frase) ele pega a lista agrupa na msm frase e cada palvra que ele juntou vai ser separada po -
print(frase.replace('Python', 'Android')) ele muda a palavra obs str é imutavel a não ser que use um função de tranformação de srt
print(frase.find('Video')) nos mostra a posição em numero da palavra 
print(frase.lower().find('video')) ele vai tranformar todas em minuscula e achar .
print(frase.split()) ele separa em lista 
dividido = frase.split()
print(dividido[0]) ele busca na lista a primeira palavra
print(dividido[2],[3]) pela o dividido 2 e me mostre a letra 3
'''

frase =('Curso em Video Python')
print(frase[3])
frase =('Curso em Video Python')
print(frase[3:13])
frase =('Curso em Video Python')
print(frase[9:21:2])
frase =('Curso em Video Python')
print(frase[:13])
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
frase = ('Curso em Video Python')
print = frase.find('deo')
frase = ('Curso em Video Python')
print = 'curso' in frase
frase = ('Curso em Video Python')
frase = ('Curso em Video Python')
frase = frase.replace('Python', 'Android')
print(frase)
