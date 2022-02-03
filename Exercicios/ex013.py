# FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONÁRIO  E MOSTRE SEU NOVO SALARIO COM 15% DE REAJUSTE.
sal = float(input('Digite o salário do colaborador: R$ '))
print(f'O salário reajustado em 15% é de R$ {sal + (sal * 15) / 100:.2f}')