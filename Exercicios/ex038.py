# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a seguinte mensagem:
# - O primeiro valor é maior que o segundo; - O segundo valor é maior que o primeiro; - Os dois valores são iguais.

print('-=' * 25)
print('COMPARADOR DE VALORES. Digite dois valores.')
print('-=' * 25)
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print(f'Os valores escolhidos foram {v1} e {v2} respectivamente.')
if v1 > v2:
    print('O primeiro valor é MAIOR que o segundo.')
elif v2 > v1:
    print('O segundo valor é MAIOR que o primeiro.')
else:
    print('Os dois valores são iguais.')
print('--FIM--')