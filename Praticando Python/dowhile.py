'''
do while

código para adivinhar um número

'''
palpite = ''
filme = 'shrek 3'

while True: # aqui testamos o codigo sem verificar
    print(' Adivinhe o filme que irei assistir hoje ')
    palpite = str(input(''))
    if palpite == filme: # aqui verificamos o nosso coódigo
        print('Voce acertou')
        break
    else:
        print(' Errado!')
else:
    print(' Erro na aplicaçao')
    print(bool(palpite))


