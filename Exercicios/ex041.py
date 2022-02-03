''' A Confederação de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de
acordo com a idade.
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Júnior
- Até 20 anos: Sênior
- Acima de 20 anos: Master
'''

from datetime import date

print('-=-' * 15)
print('Analisador de categorias COBRAN')
print('-=-' * 15)

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9:
    print(f'O(A) atleta tem {idade} anos e se enquadra na categoria MIRIM.')
elif idade <= 14:
    print(f'O(A) atleta tem {idade} anos e se enquadra na categoria INFANTIL.')
elif idade <= 19:
    print(f'O(A) atleta tem {idade} anos e se enquadra na categoria JÚNIOR.')
elif idade == 20:
    print(f'O(A) atleta tem {idade} anos e se enquadra na categoria SÊNIOR.')
else:
    print(f'O(A) atleta tem {idade} anos e se enquadra na categoria MASTER')
print('--FIM--')