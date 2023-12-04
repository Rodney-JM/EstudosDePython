from random import randint
computador = randint(0,5)
print('-=-'*20)
print('irei pensar em um número de 0 até 5, deixe-me pensar...')
print('-=-'*20)
jogador = int(input('em que numero eu pensei?'))
if jogador==computador:
    print('acertou mizeravi')
else:
    print('errou otaro, eu pensei no número {} e nao no numero {}'.format(computador,jogador))