'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional)

Adicionar docstrings da função'''


def notas(*n, sit=False):
    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n) / len(n)
    if sit:
        if turma['média'] <= 6:
            turma['situação'] = 'RUIM' 
        elif turma['média'] < 8:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'BOA'
    return turma

# Main
resp = notas(9, 4, 10, 6)
print(resp)