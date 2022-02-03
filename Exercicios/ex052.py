# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('=' * 40)
print('IDENTIFICADOR DE NÚMERO PRIMO')
print('=' * 40)
num = int(input('Digite um número: '))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m',end='')
    print(f'{n}', end=' ')
if tot <= 2:
    print(f'\n\033[30mO número {num} foi divisível {tot} vezes, por isso é um número primo.')
else:
    print(f'\n\033[30mO número {num} foi divisível {tot} vezes, por isso não é um número primo.')