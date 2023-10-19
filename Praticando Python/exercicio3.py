preco = float(input('me diga o preço do seu produto: '))
porcentagem = float(input('me diga o desconto que voce teve sob esse produto: '))
desconto = preco*porcentagem/preco
total = preco - desconto
print(f'o seu produto vai sair de {preco} para {total} reais')