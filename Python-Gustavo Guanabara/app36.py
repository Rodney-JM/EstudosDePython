a = int(input('digite um valor:'))
b = int(input('outro valor aqui'))
c = int(input(' so mais esse'))
menor= a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(' o menor valor dos numeros digitados é: {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o maior numero dos que foram digitados foi o {}'.format(maior ))