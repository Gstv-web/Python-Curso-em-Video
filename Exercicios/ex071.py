'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o VALOR A
SER SACADO (int) e o programa vai informar quantas CÉDULAS de cada valor serão entregues.
Considere que o caixa trabalha com notas de 50, 20, 10, 5 e 2.
'''

print('=' * 30)
print(f'Banco de Pobre')
print('=' * 30)
valor = int(input('Quanto deseja sacar? R$ '))
total = valor
cedula = 50
contnota = 0
while True:
    if total >= cedula:
        total -= cedula
        contnota += 1
    else:
        if contnota > 0:
            print(f'Total de {contnota} cédulas de R$ {cedula:.2f}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        contnota = 0
        if total == 0:
            break
