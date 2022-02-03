'''Crie um programa que leia NOME, SEXO e IDADE de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
- Quantas pessoas cadastradas
- A média de idade
- Uma lista com mulheres
- Uma lista com idade acima da média'''

pessoas = dict()
cadastro = list() 
# ler nome, sexo e idade várias vezes
resp = 'S'
ind = 0 # contagem de pessoas
anos = 0 # contagem de idade para média
while resp != 'n':
    pessoas['nome'] = str(input('Digite o nome da pessoa: '))
    if pessoas['nome'] == '':
        pessoas['nome'] = str(input('ERRO - Digite um nome válido: '))
    pessoas['sexo'] = str(input('Digite o sexo [M/F]: '))
    while pessoas['sexo'] not in 'mf':
        pessoas['sexo'] = str(input('ERRO - Somente inserir M ou F. Digite o sexo [M/F]: '))
    pessoas['idade'] = int(input('Digite a idade: '))
    anos += pessoas['idade']
    ind += 1
    cadastro.append(pessoas.copy())
    pessoas.clear()
    resp = str(input('Deseja continuar? [S/N]: '))
    while resp not in 'sn' or '':
        resp = str(input('ERRO - Digite apenas S ou N. Deseja continuar? [S/N]: '))
if ind == 1:
    print(f'--> Ao todo, {ind} pessoa foi cadastrada.')
else:
    print(f'--> Ao todo, {ind} pessoas foram cadastradas.')
media = anos / ind
print(f'--> A média de idade das pessoas cadastradas é de {media:.1f} anos.')
print('--> As mulheres cadastradas foram: ', end='')
for p in cadastro: # nesse caso o p vira o índice
    if p['sexo'] in 'f': # Irá buscar o valor f na key sexo
        print(f'{p["nome"]} ', end='') # irá mostra o value da key nome. DOIDERA
print()
print(f'As pessoas com idade acima da média são: ', end='')
for p in cadastro: # Mesma coisa acima. É possível iterar sobre os índices de dicionários dessa forma
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')