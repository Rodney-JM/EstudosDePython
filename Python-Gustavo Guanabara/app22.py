import random
n1 = str(input(' digite o nome do primeiro individuo: '))
n2 = str(input(' digite o nome do segundo individuo: '))
n3 = str(input(' digite o nome do terceiro individuo: '))
n4 = str(input(' digite o nome do quarto individuo: '))

alunos = [n1,n2,n3,n4]
random.shuffle(alunos)
print('a ordem de apresentaçao sera:')
print(alunos)