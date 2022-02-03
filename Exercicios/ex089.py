'''Crie um programa que leia NOME e QUATRO notas de vários alunos. No final, mostre um boletim contendo a média de cada
um e permita que o usuário possa mostrar as notas de cada aluno individualmente'''
from time import sleep
ficha = list()

print('-' * 35)
print(f'{"BOLETIM ESCOLAR":^35}')
print('-' * 35)
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    nota4 = float(input('Nota 4: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    ficha.append([nome, [nota1, nota2, nota3, nota4], media])
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for p, n  in enumerate(ficha):
    print(f'{p:<4}{n[0]:<10}{n[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 para encerrar): '))
    if opc == 999:
        print('Finalizando...')
        sleep(0.5)
        print('<Volte sempre!>')
        break
    else:
        if opc <= len(ficha) - 1:
            print(f'{ficha[0][1]}')


