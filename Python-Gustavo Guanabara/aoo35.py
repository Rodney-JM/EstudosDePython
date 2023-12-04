from datetime import date
ano = int(input('qual ano voce quer analisar?'))
if ano%4==0 and ano %100 !=0 or ano%400==0:
    print('esse ano é bisexto')
else:
    print('esse ano nao é bisexto ')