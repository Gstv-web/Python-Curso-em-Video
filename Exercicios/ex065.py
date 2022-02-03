'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digi-
tar valores.
'''

r = 'S'
maior = 0
menor = 0
soma = 0
cont = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    if cont == 1: #Isso aqui é muito importante: SE o contador = 1, ambos os valores recebem n
        menor = maior = n
    else: # Assim posso fazer a identificação dos maiores e menores valores sem precisar criar array
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
    soma += n
    r = input('Deseja adicionar outro valor? [S/N]').upper().strip()
print(f'A soma dos valores inseridos é de {soma}.')
print(f'Você digitou {cont} números e a média entre os valores inseridos é de {soma / cont}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')