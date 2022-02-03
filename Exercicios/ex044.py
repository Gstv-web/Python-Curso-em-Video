''' Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de paga-
mento.
- À vista (dinheiro/cheque): 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
'''

normal = float(input('Digite o valor do produto: R$ '))
pag = int(input('''Escolha a forma de pagamento:
[ 1 ] - À vista Cheque/Dinheiro
[ 2 ] - À vista Cartão
[ 3 ] - Parcelado
'''))

if pag == 1:
    print(f'O preço final é de R$ {normal - (normal * 10 / 100):.2f}. Foi concedido 10% de desconto.')
elif pag == 2:
    print(f'O preço final é de R$ {normal - (normal * 5 / 100):.2f}. Foi concedido 5% de desconto.')
else:
    vezes = int(input('Em quantas vezes a compra será parcelada? '))
    if vezes == 2:
        print(f'O preço final do produto é de R$ {normal:.2f}. {vezes}x de R$ {normal / 2:.2f}')
    else:
        print(f'O preço final do produto é de R$ {normal + (normal * 15 / 100):.2f}. {vezes}x de {normal / vezes:.2f}. Foi acrescentado 15% de juros.')