'''
Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente
'''

# Digitar vários valores
valores = []
resp = 's'.upper()
while resp == 'S':
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor duplicado. Não será adicionado.')
    else:
        valores.append(n)
    resp = input('Deseja continuar? S/N: ').upper()
print('-=' * 35)
print(f'Você digitou os valores {sorted(valores)}')