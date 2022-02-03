# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print(f'A parede tem uma dimensão de {altura}x{largura} e sua área é de {area}m².')
print(f'Para pintar essa parede, será necessário aproximadamente {tinta:.2f}l de tinta.')