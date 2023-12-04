num = int(input('Digite aqui o número que deseja converter: '))
print('''
[1] CONVERTER PARA BINÁRIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL
''')
opcao = int(input('Qual opção deseja? '))
if opcao==1:
    print(' O número {} em binário ficaria {}'.format(num,bin(num)[2:]))
elif opcao==2:
    print('O número {} em octal ficaria {}'.format(num,oct(num)[2:]))
elif opcao==3:
    print('O número {} em hexadecimal ficaria {}'.format(num,hex(num)[2:]))
