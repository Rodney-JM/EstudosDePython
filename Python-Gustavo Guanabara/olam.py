idade_cibele = int(input())
idade_camila = int(input())
idade_celeste = int(input())

# Verifica a idade de Camila
if idade_cibele < idade_camila < idade_celeste or idade_celeste < idade_camila < idade_cibele:
    print(idade_camila)
elif idade_camila < idade_cibele < idade_celeste or idade_celeste < idade_cibele < idade_camila:
    print(idade_cibele)
else:
    print(idade_celeste)