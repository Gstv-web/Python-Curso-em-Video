'''
Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS. O programa deverá perguntar se o USUÁRIO vai continuar.
No final, mostre:
- Qual é o TOTAL GASTO na compra;
- Quantos produtos custam MAIS de R$100,00.
- Qual é o NOME do produto mais BARATO;
'''

print('-' * 25)
print('ESTATÍSTICA EM PRODUTOS')
print('-' * 25)
totalcompra = contocen = contcompra = maisbarato = 0

while True:
    produto = str(input('Produto: ')).capitalize()
    preço = float(input('Preço: R$ '))
    totalcompra += preço
    contcompra += 1
    if preço > 100:
        contocen += 1
    if contcompra == 1:
        barato = produto
        maisbarato = preço
    if preço < maisbarato:
        barato = produto
        maisbarato = preço
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).upper()
    if r == 'N':
        break
print('-' * 30)
print(f'O total gasto nas comprar foi de R$ {totalcompra:.2f}.')
print(f'{contocen} produtos custam mais de R$ 100,00.')
print(f'O produto mais barato comprado foi {barato}, que custa R$ {maisbarato}.')