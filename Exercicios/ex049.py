# Refaça o desafio 009, mostrando a tabuada de um número que um usuário escolher, mas com o laço for

n = int(input('Digite um número para mostrar a tabuada: '))
for c in range(0, 11):
    print(f'{n}  x {c:2} = {n * c}')