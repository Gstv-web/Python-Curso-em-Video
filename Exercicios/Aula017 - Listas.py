# listas são variáveis compostas, mas ao ivés de () usa-se []
# São mutáveis, ou seja, posso alterar os valores dentro da lista

lanche = ['Hamburguer', 'Pizza', 'Refrigerante', 'Pudim']
print(lanche)
lanche[3] = 'Brigadeiro' # troca o elemento [3] para outro.
print(f'{lanche} Troquei pudim pelo brigadeiro')
lanche.append('Cookie') # adiciona um valor à lista, sempre no final dela
print(f'{lanche} Botei mais uma váriável')
lanche.insert(2, 'Bolo') # adiciona um valor à lista no índice que desejar
print(f'{lanche} Botei um bolo na posição 3 (índice 2) porque eu quis que fosse assim')
del lanche[2] # apaga um valor da lista no indice que desejar
# lanche.pop apaga o ultimo valor da lista, mas posso colocar o índice () também
# lanche.remove() apaga o valor que desejar, porém tem que ser específico (ex. lanche.remove('Pizza')
print(f'{lanche} Tirei o bolo com o comando del')
valores = list(range(6,11)) # declara uma lista em uma nova variável.
print(f'{valores} Lista criada com range(6, 11)')
lanche.sort() # ordem alfanumérica
print(f'{lanche} Botei em ordem alfanumérica')
lanche.reverse() # ordem contrária
print(f'{lanche} E agora inverti a ordem. Como ela foi colocada em alfanumérica primeiro, ela inverte por conta dessa última alteração, caso contrário seria sobre o original')
print(f'Há {len(lanche)} elementos na lista lanche')
if 'Pizza' in lanche: #Bom termo para apagar valores em listas grandes encontrando o que quiser
    lanche.remove('Pizza')
print(lanche)
print('=' * 50)

compra = list() # Também serve para laços
for cont in range(0,5):
    compra.append(input('Digite o nome do produto: '))
print(compra)
for pos, produto in enumerate(compra):
    print(f'Na posição {pos} temos o valor {produto}.')
