'''
Operadores logicos e tipo boolean
Em python, boolean = true or false
'''

'''
Operadores logicos
and
or
not
'''

'''
Tabela da verdade
verdadeiro e verdadeiro = verdadeiro
se tiver algo falso na equaçao, o resultado sera falso'''

'''tabela da verdade usando o or

true or true= true
true or false = true
false or false = falso
false or true = true
'''

nome_usuario1= input('nome: ')
senha_usuario1 = input('senha: ')

if nome_usuario1 =='Vanderlei' and senha_usuario1=='123456':
    print('acesso aprovado')
else:
    print('tente novamente maais tarde')