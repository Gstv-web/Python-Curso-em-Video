'''Crie um programa que leia uma matriz de dimensão 3x3 e preencha com valores pelo teclado. No final, mostre a matriz
na tabela, com a formatação correta.'''
'''
linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
num = 0
for c in range(0, len(linha1)):
    if c == 0:
        num = int(input(f'Digite o valor para a posição [0,{c}]: '))
        linha1[0].append(num)
    elif c == 1:
        num = int(input(f'Digite o valor para a posição [0,{c}]: '))
        linha1[1].append(num)
    elif c == 2:
        num = int(input(f'Digite o valor para a posição [0,{c}]: '))
        linha1[2].append(num)
for c in range(0, len(linha2)):
    if c == 0:
        num = int(input(f'Digite o valor para a posição [1,{c}]: '))
        linha2[0].append(num)
    elif c == 1:
        num = int(input(f'Digite o valor para a posição [1,{c}]: '))
        linha2[1].append(num)
    elif c == 2:
        num = int(input(f'Digite o valor para a posição [1,{c}]: '))
        linha2[2].append(num)
for c in range(0, len(linha3)):
    if c == 0:
        num = int(input(f'Digite o valor para a posição [2,{c}]: '))
        linha3[0].append(num)
    elif c == 1:
        num = int(input(f'Digite o valor para a posição [2,{c}]: '))
        linha3[1].append(num)
    elif c == 2:
        num = int(input(f'Digite o valor para a posição [2,{c}]: '))
        linha3[2].append(num)
print(linha1)
print(linha2)
print(linha3)'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digita o valor para a posição [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end=' ')
    print()
