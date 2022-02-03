# Faça um programa que leia um número qualquer e mostre seu fatorial
from math import factorial
n = int(input('Digite um número para ver seu fatorial: '))
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    c -= 1
print(factorial(n))