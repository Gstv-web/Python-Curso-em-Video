# Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.500,00, o aumento é de 10%, para inferiores ou iguais, o aumento é de 15%

print('-=-CÁLCULO DE AUMENTO SALARIAL-=-')
sal = float(input('Digite o salário do colaborador: '))
sal15 = sal * 15 / 100
sal10 = sal * 10 / 100

if sal <= 1500:
    print(f'O aumento salarial será de 15%, equivalente a R$ {sal15:.2f}.')
    print(f'Salário final: R$ {sal + sal15:.2f}.')
else:
    print(f'O aumento salarial será de 10%, equivalente a R$ {sal10:.2f}.')
    print(f'Salário final: R$ {sal + sal10:.2f}.')
print('--FIM--')