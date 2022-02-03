# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE HÁ "SILVA" NO NOME.
nome = input('Digite seu nome completo: ')
print(f'Seu nome tem Silva? {"Silva" in nome.lower()}')