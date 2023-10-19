'''
if, else e elif 

elif= outras condiçoes que podem ser cumpridas dentro
do if 

'''
import random
lista = [1, 2, 3, 4, 5, 6, 7]
lista_sorteada = random.choice(lista)
escolha_jogador = str(input('Deseja sortear um numero? S/N ')).lower
if escolha_jogador == 's' or 'sim':
    print(f' Seu número sorteado é: {lista_sorteada}')
else:
    print(' OK, tente novamente se preferir')

'''
se quiser reduzir o if e o else basta
print('b') if b< a else print('a')'''

