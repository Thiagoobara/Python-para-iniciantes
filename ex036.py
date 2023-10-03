'''
Cores no terminal
style           
0 Nome
1 bold
4 underline
7 negative
text
30
31
32
33
34
35
36
37
back
40
41
42
43
44
45
46
47

teste\033[0;30;41m
teste\033[4;33;44m
teste\033[1;35;43m
teste\033[30;42m
teste\033[m
teste\033[7;30m
'''

print('\033[31mOla! Mundo')
print('\33[32;43mOla, Mundo!\33[m')
print('\033[4;36;41mOla! Mundo!\33[m')