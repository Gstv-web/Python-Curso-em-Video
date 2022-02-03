# Todos os conceitos das listas são aplicadas aos dicionários
# A diferença é que nos dicionários, os índices podem ser personalizados.
# É possível fechar as chaves em outra linha
# 'Keys' é o nome do indice que eu dei. No caso, 'nome'.
# 'Values' é o conteúdo do índice, ou seja, o o que for atribuído ao keys
# 'Items' são ambos.

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 29}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.') # Aspas duplas sempre que houver um print formatado
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('--------------')
for k in pessoas.keys():
    print(k)
print('Aqui eu mostrei o nome dos índices dentro de um for para cada índice dentro da biblioteca.')
print('--------------')
for v in pessoas.values():
    print(v)
print('Aqui eu mostrei os valores que tem nos índices ')
print('--------------')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('Usando o "for" combinado com "pessoas.items()" eu consigo mostrar tanto as keys quanto os values.')
print('--------------')
del pessoas['idade']
print(f'{pessoas} - Usei o comando del para tirar a idade (pode ser qualquer key)')
print('--------------')
pessoas['nome'] = 'Kleber'
print(f'{pessoas} - Mudei o value da key na biblioteca "pessoas"')
print('--------------')
pessoas['peso'] = 60
print(f'{pessoas} Adicionei um índice chamado peso')
print(' * ' * 10)
print('Dois dicionários em uma lista')
brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(f'{brasil[0]["sigla"]} - Também posso escolher o que mostrar')
# lista.append(dicionário.copy()) - Caso eu precise incluir um dicionário em uma lista em algum momento.