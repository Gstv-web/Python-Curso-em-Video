'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

listagem = ('Mouse', 59.90, 'Teclado', 129.90, 'Mousepad', 34.90, 'Headphone', 229.90, 'Placa de vídeo', 499.90,
          'Monitor 24"', 799.90, 'Microfone', 89.90, 'Câmera', 129.90)

print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #^ centraliza 40 número de espaços
print('=' * 40)
for produto in range(0, len(listagem)):
    if produto % 2 == 0:
        print(f'{listagem[produto]:.<30}', end=f'' ) # . pontos < Alinha o texto a esquerda 30 espaços
    else:
        print(f'R$ {listagem[produto]:>7.2f}') # > alinha pra direita 7 espaços .2f casas decimais
