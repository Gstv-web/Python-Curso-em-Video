'''Faça um programa que leia o nome e média de um aluno, guardando também sua situação em um dicionário. No final, mos-
tre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situaçao'] = 'aprovado'
else:
    aluno['situaçao'] = 'reprovado'
print('--------------------------')
for a, n in aluno.items():
    print(f'- {a} é igual a {n}.')
