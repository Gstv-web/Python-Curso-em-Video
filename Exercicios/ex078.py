'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e menor valor digitado e suas respectivas posições na lista.
'''

valor = list()
maior = menor = 0
for c in range(0,5):
    valor.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        if valor[c] < menor:
            menor = valor[c]
print(f'Os números digitados são {valor}')
print(f'O maior valor digitado foi {maior} e está nas posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} e está nas posições ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}...', end='')