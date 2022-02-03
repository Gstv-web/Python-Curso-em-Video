'''Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com IDADE) em um dicionário.
Se por acaso a CTPS for 0, terminar o programa, caso contrário, pedir o ano de contratação e o último salário. Botar na tela idade e com quantos anos irá se aposentar '''
from datetime import date

cadastro = {}
# Pedir o nome
cadastro['nome'] = str(input('Digite o nome: '))
# Pedir o ano de nascimento
cadastro['idade'] = date.today().year - int(input('Digite o ano de nascimento: ')) 
# Pedir carteira de trabalho
cadastro['ctps'] = int(input('Digite o número da CTPS (0 não tem): '))
if cadastro['ctps'] != 0:
    #pedir ano de contratação
    cadastro['inicio'] = int(input('Digite o ano de contratação: '))
    #pedir o salário
    cadastro['salario'] = float(input(f'Digite o salário: '))
    cadastro['apos'] = cadastro['idade'] + 35 
    for k, v in cadastro.items():
        print(f'- {k} tem valor {v}')
else:
    for k, v in cadastro.items():
        print(f'- {k} tem valor {v}')