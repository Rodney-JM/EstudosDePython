fr = str(input(' digite uma frase a seguir: ')).lower().strip()
print('nessa frase o A aparece {} vezes'.format(fr.count('a')))
print(' nessa frase o a aparece pela primeira vez na posiçao {}'.format(fr.find('a')+1))
print(' o A aparece pela ultima vez na posiçao {}'.format(fr.rfind('a')+1 ))