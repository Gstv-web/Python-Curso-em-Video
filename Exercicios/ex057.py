# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores F e M. Caso esteja errado, peça a digitação
# novamente até ter um valor correto


s = str(input('Digite o sexo da pessoa [F/M]: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Dados inválidos. Digite novamente: ')).upper().strip()[0]
print(f'Sexo {s} registrado com sucesso.')