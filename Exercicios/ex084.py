''' Faça um programa que leia nome e peso de várias pessoas. No final, mostre:
- Quantas pessoas foram cadastradas;
- Uma listagem com as pessoas mais pesadas;
- Uma listagem com as pessoas mais leves;
'''

temp = []
main = []
maior = menor = 0

print('=' * 75)
print('Nomes e Pesos - Uma ideia de como inputar dados e de mostrá-los')
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(main) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    main.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()
    if resp in 'Nn':
        break
print('=' * 75)
print(f'Foram cadastradas {len(main)} pessoas.')
print(f'O maior peso encontrado foi de {maior}kg. Peso de ', end='')
for p in main:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso encontrado foi de {menor}kg. Peso de ', end='')
for p in main:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print('--FIM--')