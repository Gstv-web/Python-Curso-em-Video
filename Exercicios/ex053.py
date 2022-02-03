# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
dividido = frase.split()
junto = ''.join(dividido)
inverso = ''.upper()
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')