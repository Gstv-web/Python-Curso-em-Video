'''Crie um programa que leia sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente'''

numeros = [[], []] #Lista dentro da lista
num = 0
for c in range(1, 8):
    num = int(input(f'{c}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('-=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os pares digitados são: {numeros[0]}')
print(f'Os ímpares digitados são: {numeros[1]}')
print('--FIM--')