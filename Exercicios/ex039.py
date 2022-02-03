''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é hora de se alistar;
- Se já passou o tempo de alistamento.
O programa também deverá mostrar o tempo que falta ou faltou do prazo
'''

from datetime import date

print('-*' * 20)
print('Verificação de alistamento lixo')
print('-*' * 20)
ano = int(input('Digite o ano de nascimento do coitado: '))
base = date.today().year
idade = base - ano

if idade < 18:
    print(f'O jovem ainda não completou 18 anos e não precisa se alistar. Falta(m) {18 - idade} ano(s) para o alistamento.')
elif idade > 18:
    print(f'O arrombado já deveria ter feito o alistamento há pelo menos {idade - 18} ano(s). Cadeia nele!')
else:
    print('Este é o ano para o alistamento. Está na hora!')
print('--FIM--')