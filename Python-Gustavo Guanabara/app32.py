num = int(input('Qual a velocidade atual do carro?'))
multa= (num-80)*7
if num<=80:
    print('parabens,voce esta dentro do limite de velocidade!!')
else:
    print('ishhh,voce acabou de ultrPssar o limite de velocidade dessa rodovia, a sua multa sera de R${:.2f}'.format(multa))