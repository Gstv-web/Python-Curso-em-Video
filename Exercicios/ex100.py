'''Faça um programa que tenha uma lista chamada números e duas funções chamads sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro
da lista e a segunda vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint

numeros = list()

def sorteio():
    print(f'Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num}', end=' ')  

def somapar():
    soma = 0
    for p in numeros[:]:
        if p % 2 == 0:
            soma += p
    print(f'\nSomando todos os valores pares de {numeros}, temos {soma}.')

sorteio()
somapar()