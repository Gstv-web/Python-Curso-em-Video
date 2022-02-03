"""
CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao todo, sem contar espaços;
- Quantas letras tem o primeiro nome.
"""
nome = "José Gustavo Oliveira da Silva"
print(nome)
print(nome.upper())
print(nome.lower())
print(f'O nome possui {len(nome)-nome.count(" ")} letras') #ignorando espaços dentro de uma string
# print(f'O primeiro nome possui {len(nome[:4])} letras')
print(f'O primeiro nome possui {nome.find(" ")} letras.')