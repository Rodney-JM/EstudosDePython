nome = input('digite o seu nome a seguir por favor: ')
print('o seu nome em maiusculo é {}'.format(nome.upper()))
print(' o seu nome em minusculas sera {}'.format(nome.lower()))
print(' o seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print(' o seu primeiro nome possui {} letras'.format(nome.find(' ')))