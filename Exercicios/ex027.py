# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE
n = str(input('Digite um nome e sobrenome: ')).strip()
nome = n.split()
print(f'Olá, {n}!')
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')