cor_alien = 'vermelho'
if cor_alien== 'verde':
    print('voce ganhou 5 pontos !')
elif cor_alien =='amarelo':
    print('voce acabou de ganhar 10 pontos')
elif cor_alien== 'vermelho':
    print('voce ganhou 15 pontos')

age = int(input('digite a sua idade: '))
if age>= 2 and age< 4:
    print('voce é uma criança')
elif age>= 4 and age< 13:
    print('voce é um garoto(a)')
elif age>= 13 and age< 20:
    print('voce é um adolescente')
elif age>= 20 and age< 65:
    print('voce é um adulto')
elif age>= 65:
    print('voce é um idoso')

favorite_fruits = ['banana', 'maçã', 'mamão', 'melancia', 'pitaya']
fruit = input('Digite uma fruta: ').lower()
if fruit== 'banana' or 'maçã' or 'mamão' or 'melancia' or 'pitaya':
    print('amo essa fruta')
    
