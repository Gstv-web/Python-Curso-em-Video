# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE UM NOVO PREÇO COM 5, 10 E 15% DE DESCONTO
preço = float(input('Digite o preço do produto: R$'))
print(f'O valor digitado é de R${preço}.')
print(f'Com 5% de desconto, o valor fica R${preço - (preço * 5) / 100:.2f}')
print(f'Com 10% de desconto, o valor fica R${preço - (preço * 10) / 100:.2f}')
print(f'Com 15% de desconto, o valor fica R${preço - (preço * 15) / 100:.2f}')