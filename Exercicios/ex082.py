'''
Crie um programa que vai ler vários números e colocá-los em uma lista. Depois disso, crie duas listas que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

geral = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    geral.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = input('Deseja continuar? S/N: ')
    if resp in 'nN':
        break
print('=' * 30)
print(f'A lista com todos os números digitados: {geral}')
print(f'A lista com apenas pares: {par}')
print(f'A lista com apenas ímpares: {impar}')