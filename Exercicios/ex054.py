# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores

from datetime import date

base = date.today().year
c1 = 0
c2 = 0
print('Identificado de maioridade')

for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if base - ano < 18:
        c1 += 1
    else:
        c2 += 1
print(f'Identificamos {c1} pessoa(s) menor de idade e {c2} pessoa(s) maior de idade.')