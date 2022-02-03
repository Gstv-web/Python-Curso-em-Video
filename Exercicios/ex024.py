# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA COM O NOME 'SANTO'
cidade = input('Digite uma cidade: ').strip()
print(cidade[:5].upper() == 'SANTO')