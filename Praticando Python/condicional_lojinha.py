print('Escolha o que você vai querer:')
escolha_1 = input('| calça | bermuda | moletom | ')
escolha_2 = input('| camisa | camiseta | casaco | ')

calça_p, bermuda_p, camisa_p, camiseta_p, moletom_p, casaco_p = 80, 50, 40, 35, 55, 90

ps_1 = 0
ps_2 = 0

if escolha_1 == 'calça':
    ps_1 = calça_p
elif escolha_1 == 'bermuda':
    ps_1 = bermuda_p
elif escolha_1 == 'moletom':
    ps_1 = moletom_p

if escolha_2 == 'camisa':
    ps_2 = camisa_p
elif escolha_2 == 'camiseta':
    ps_2 = camiseta_p
elif escolha_2 == 'casaco':
    ps_2 = casaco_p

print(f'A sua {escolha_1} e o seu {escolha_2} custarão {ps_1 + ps_2} reais')
