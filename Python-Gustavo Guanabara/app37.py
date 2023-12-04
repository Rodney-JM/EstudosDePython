salario = float(input('escreva para mim o seu salario neste momento'))
if salario<1250:
    print('agora o seu salario sera de R$ {:.2f}'.format(salario+15*salario/100))
if salario>1250:
    print('o seu salario sera de R$ {}'.format(salario+10*salario/100))