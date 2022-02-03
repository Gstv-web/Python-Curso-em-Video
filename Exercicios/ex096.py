'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno'''

def área(l, c): # sabendo que para calcular uma área eu preciso de duas medidas, coloco dois parâmetros
      a = l * c # mesmo não havendo variável definida ainda, boto elas aqui, lembrando de usá-las posteriormente
      print(f'A área de um terreno {l}m x {c}m é de {a}m².')

print(' Controle de Terrenos ')
print('-' * 22)
l = float(input('Largura: ')) # as variáveis são criadas no código
c = float(input('Comprimento: '))
área(l, c)