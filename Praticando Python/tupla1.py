# Definindo a tupla com os cinco pratos básicos
pratos_basicos = ('Arroz', 'Feijão', 'Frango', 'Salada', 'Macarrão')

# Exibindo cada prato oferecido pelo restaurante usando um loop for
print("Pratos oferecidos pelo restaurante:")
for prato in pratos_basicos:
    print(prato)

# Tentando modificar um dos itens da tupla - Isso resultará em um erro!
# Você verá que o Python rejeita a mudança.
try:
    pratos_basicos[0] = 'Sushi'
except TypeError:
    print("Você não pode modificar os itens da tupla diretamente!")

# Revisando o cardápio do restaurante substituindo dois itens
pratos_basicos = ('Arroz Integral', 'Feijão Preto', 'Peixe Grelhado', 'Legumes', 'Lasanha')

# Exibindo cada item do cardápio revisado usando um loop for
print("\nCardápio revisado do restaurante:")
for prato in pratos_basicos:
    print(prato)






