''' Faça um programa que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''

from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.35)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'- Foram informados {cont} valores.')
    print(f'A maior valor informado foi {maior}')


maior(4, 5, 9, 1, 6)
maior(0, 5, 4, 8, 6, 3)
maior(5, 1)
maior()