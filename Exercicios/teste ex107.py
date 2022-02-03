'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
 Faaça também um programa que importe esse módulo e use algumas dessas funções'''

from ex107 import moeda

valor = int(input('Digite um preço: R$ '))

print(f'O dobro de R$ {valor:.2f} é R$ {moeda.dobro(valor):.2f}')
print(f'A metade de R$ {valor:.2f} é R$ {moeda.metade(valor):.2f}')
print(f'Reduzindo 16% de R$ {valor}, temos {moeda.diminuir(valor, 16)}')
print(f'Aumentando 22% de R$ {valor}, temso {moeda.aumentar(valor, 22)}')