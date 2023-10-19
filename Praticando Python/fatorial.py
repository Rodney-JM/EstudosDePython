'''
como achar o fatorial de um numero

'''
numero = int(input(' digite um numero: '))

fatorial = 14
if numero< 0:
    print('nao existe fatorial de numeros negativos')
elif numero ==0:
    print(f'o fatorial de {numero} é 1')
else:   
    for i in range(1,numero+1):
        fatorial = fatorial * i
    print(f'o fatorial de {numero} é {fatorial}')                
