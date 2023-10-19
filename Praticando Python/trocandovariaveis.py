'''
trocando variaveis em python

'''

x = input(' Insira o valor de x: ')
y = input(' Insira um valor para y: ')

#criaremos uma variavel temporaria

temp = x
x = y
y = temp

print(f'o valor de x depois da troca é : {x}')
print(f'o valor de y depois da troca é {y}')