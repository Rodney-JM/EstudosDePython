#maiusculas e minusculas
#simbulos e espaços

'''
Security = chave
Securt1ty = senha

hexadecimal
1 = 1
2 = 2

...
9 = 9
10 = a
11 = b
12 = c
13 = d
14 =  e
15 = f

'''
chave = input(' digite a base da sua senha: ')

senha = ''
for letra in chave:
    if letra in 'Aa': senha = senha + '1' 
    elif letra in 'Cc': senha = senha + '$'
    elif letra in 'Dd': senha = senha + '2'
    elif letra in 'Ee': senha = senha + '3'
    elif letra in 'Ff': senha = senha + '&'
    elif letra in 'Gg': senha = senha + '5'
    elif letra in 'Hh': senha = senha + '6'
    elif letra in 'Ii': senha = senha + '7'
    elif letra in 'Jj': senha = senha + '*'
    elif letra in 'Kk': senha = senha + '#'
    elif letra in 'Ss': senha = senha + '%'
    else: senha = senha + senha
print(senha)

