print('-='*20)
print('analisador de triangulos...')
print('-='*20)
n1 = float(input('coloque o valor do primeiro numero'))
n2 = float(input('coloque o segundo agora'))
n3 = float(input('o valor do terceiro agora'))
if n1< n2+n3 and n2< n1+n3 and n3< n1 + n2:
    print('parabens, os segmentos acima podem criar um triangulo')
else:
    print('os valores digitados nao formam um triangulo')