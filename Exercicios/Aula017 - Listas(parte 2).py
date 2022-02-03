# Listas dentro de listas

pessoas = [['Pedro', 21], ['Maria', 27], ['João', 25]]
print(f'{pessoas[:]} Devo usar [][] como indice, o primeiro para a "lista de fora" e a segunda para "de dentro"')

print('=' * 50)

teste = list() # Criei uma lista
teste.append('Gustavo')
teste.append(29) # Botei essas variáveis na lista
galera = list() # Criei outra lista
galera.append(teste[:]) # Copiei a primeira lista dentro desta lista
teste[0] = 'Ana'
teste[1] = 31 # Mudei as variáveis
galera.append(teste[:]) # E adicionei à nova lista
print(galera) # Duas listas em uma