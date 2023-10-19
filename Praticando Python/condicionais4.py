#Primeira atividade
users = ['magelagan', 'admin', 'luffos', 'oniway', 'telex']
for user in users:
    if user=='admin':
        print('Olá, admin, gostaria de ver um relatório de status?')
    elif user in users:
        print('Seja Bem-vindo(a), '+ user)

if len(users)== 0:
    print('Precisamos encontrar novos usuários!')
#Segunda atividade 
current_users = ['Maicon', 'Pedro', 'Rosa', 'Rodolfo', 'Zacarias']
new_users = ['Miguel', 'Tadeu', 'Aristeu', 'Pedro', 'Zacarere']

for user in new_users:
    if new_users in current_users:
        print('Mude o nome de perfil por gentileza!')
    else:
        print('Seja bem-vindo(a), '+ user)

#Terceira atividade

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number== 1:
        print('1st')
    elif number== 2:
        print('2nd')
    elif number== 3:
        print('3rd')
    else:
        print('{}th'.format(number))