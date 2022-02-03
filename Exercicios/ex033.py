# Faça um programa que leia três números diferentes e mostre qual é o maior e o menor

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
print('Analisando números...')
sleep(1)

if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}.')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}.')
elif n3 > n1 and n3 > n2:
    print(f'O maior número é {n3}.')

if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor número é {n3}')