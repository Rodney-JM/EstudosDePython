convidados = ['luf', 'nam', 'zor', 'bro', 'muri', 'mat']

convidados.remove('mat')
print(' O convidado mat não poderá comparecer a festa')
convidados.append('tal')
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[0]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[1]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[2]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[3]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[4]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[5]))
print('Será possível convidar mais pessoas !')
convidados.insert(0, 'danilo')
convidados.insert(2, 'omaiko')
convidados.append('takilos')


print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[0]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[1]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[2]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[3]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[4]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[5]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[6]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[7]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[8]))

convidadospop = convidados.pop()
print('Sinto muito por não poder te receber {}'.format(convidadospop))
convidadospop = convidados.pop()
print('Sinto muito por não poder te receber {}'.format(convidadospop))
convidadospop = convidados.pop()
print('Sinto muito por não poder te receber {}'.format(convidadospop))
convidadospop = convidados.pop()
print('Sinto muito por não poder te receber {}'.format(convidadospop))
convidadospop = convidados.pop()
print('Sinto muito por não poder te receber {}'.format(convidadospop))
convidadospop = convidados.pop()
print('Sinto muito por não poder te receber {}'.format(convidadospop))
convidadospop = convidados.pop()
print('Sinto muito por não poder te receber {}'.format(convidadospop))
print(convidados)

print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[0]))
print('Olá, {}, seja bem-vindo a minha festa, hoje voce foi convidado para esse evento'.format(convidados[1]))

del convidados[0]
del convidados[0]
print(convidados)