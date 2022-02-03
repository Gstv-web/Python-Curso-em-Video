# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DE CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA
import math
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
print(f'A Hipotenusa vai medir {math.hypot(co, ca):.2f}')