'''
Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário deseja continuar. No final, mostre:
- Quantas pessoas tem mais de 18 ANOS;
- Quantos HOMENS foram cadastrados;
- Quantas MULHERES tem menos de 20 ANOS.
'''
print('-' * 20)
print('ANÁLISE DE DADOS EM GRUPO')
print('-' * 20)

contm = conth = conti = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
    if idade > 18:
        conti += 1
    if sexo == 'M':
        conth += 1
    if idade < 20 and sexo == 'F':
        contm += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).upper()
    if r == 'N':
        break
    print('-' * 20)
print('-' * 20)
print(f'Foram cadastrados {conth + conti + contm} pessoas.')
print(f'{conti} pessoas cadastradas têm mais de 18 anos.')
print(f'Das {conth + conti + contm} pessoas cadastradas, {conth} são homens.')
print(f'Das {conth + conti + contm} pessoas cadastradas, {contm} são mulheres com menos de 20 anos.')