# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO
from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer:'))
s = sin(radians(ang))
print(f'O ângulo de {ang} tem o SENO de {s:.2f};')
c = cos(radians(ang))
print(f'O ângulo de {ang} tem o COSSENO de {c:.2f};')
t = tan(radians(ang))
print(f'O ângulo {ang} tem a TANGENTE de {t:.2f}.')

#SE EU TIVESSE USADO O import math, eu deveria utilizar os módulos ali embaixo com math.sin, por exemplo