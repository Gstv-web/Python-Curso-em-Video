'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de núme-
ros gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: ', end='')
for num in n:
    print(f'{num}', end=' ')
print(f'\nO maior número sorteado foi: {max(n)}') # max() mostra o maior valor dentro de uma tupla
print(f'O menor número sorteado foi: {min(n)}') # min() mostra o menor valor dentro de uma tupla