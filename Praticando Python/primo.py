'''descobrir se um numero é primo ou nao

'''

print(30 * '-')
num = int(input(' Digite um numero: '))
if num > 1:
    for i in range(2,num):
        if(num% i)== 0:
            print('esse numero nao é primo')
            break
        else:
            print(' esse numero é primo')
else:
    print('esse numero nao é primo')

print(30*'-')
