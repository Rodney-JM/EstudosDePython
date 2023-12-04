val = float(input('Insira o valor da casa:'))
sal = float(input('Insira o seu salário: '))
temp = float(input(' Insira o tempo necessário para voce pagar a casa: '))
prest = (val/temp)/12
sal1 = sal/100*30
if prest> sal1:
    print('Por ter que pagar {} por mes, é impossivel realizar esse empréstimo '.format(prest))
else:
    print('parabens, voce cumpre os requisitos, então será possível realizar esse empréstimo')