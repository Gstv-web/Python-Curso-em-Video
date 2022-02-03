'''Crie um programa que leia uma matriz de dimensão 3x3 e preencha com valores pelo teclado. Mostre a matriz
na tabela, com a formatação correta.
No final, mostre:
- A soma de todos os valores PARES digitados;
- A soma de todos os valores da TERCEIRA coluna;
- O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
maior = 0
scol = 0
for l in range(0,3): # l vai fazer x vezes o c
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]: '))
        if matriz[1][c] > maior:
            maior = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print(f'A soma dos números pares é igual a {soma}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma de todos os valores da terceira coluna é de {scol}')
print(f'O maior valor da segunda linha é {maior}')

