pizzas = ['calabreza','mussarela', 'carne de sol']
for pizza in pizzas:
    print('gosto de pizza de '+ pizza)
print('eu adoro muito pizzas!')

animais = ['cachorro', 'gato', 'pássaro']
for animal in animais:
    print('Um '+ animal+' seria um ótimo animal de estimação')
print(' Adoraria adotar qualquer um desses animais!')

par_numbers = list(range(2,11,2))
print(par_numbers)

for square in range(1,11):
    square = square**2
    print(square)

for i in range(1,21):
    print(i)

'''for i in range (1,1000001):
    print(i)
    print (min(i))
    print(max(i))
    print(sum(i))'''

for x in range(1,21,2):
    print(x)

for x in range(3,31,3):
    print(x)

for i in range(1,11):
    i = i**3
    print(i)

i = [i**3 for i in range(1,11)]
print(i)
friend_pizzas = pizzas[:]
pizzas.append('dois queijos')
friend_pizzas.append('peperoni')

for pizza in pizzas:
    print('As minhas pizzas favoritas são: '+ pizza)

for pizza2 in friend_pizzas:
    print('As pizzas favoritas do meu amigo são: '+pizza2) 