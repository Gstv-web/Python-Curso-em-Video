# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO ENTRE 0 E 9999 E MOSTRE NA TELA CADA DÍGITO SEPARADO
numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'analisando o número {numero}...')
print(f'Unidade: {u};')
print(f'Dezena: {d};')
print(f'Centena: {c};')
print(f'Milhar: {m}.')