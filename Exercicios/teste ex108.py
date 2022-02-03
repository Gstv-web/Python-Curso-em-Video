'''Ex 107 com formatação'''

from ex108 import moeda

valor = int(input('Digite um preço: R$ '))

print(f'O dobro de R$ {moeda.moeda(valor)} é R$ {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de R$ {moeda.moeda(valor)} é R$ {moeda.moeda(moeda.metade(valor))}')
print(f'Reduzindo 16% de R$ {moeda.moeda(valor)}, temos {moeda.moeda(moeda.diminuir(valor, 16))}')
print(f'Aumentando 22% de R$ {moeda.moeda(valor)}, temso {moeda.moeda(moeda.aumentar(valor, 22))}')