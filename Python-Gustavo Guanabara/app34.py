km = int(input('coloque a seguir a quantidade de kilometros peercorridos durante a viagem : '))
n1 = km*0.5
n2 = km*0.45
if km<=200:
    print('o preço da sua viagem sera de R${}'.format(n1))
else:
    print('o preço da sua viagem sera de R${}'.format(n2))