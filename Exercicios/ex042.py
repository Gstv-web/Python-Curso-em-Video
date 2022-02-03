# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo e
# informar que tipo de triângulo é.

from time import sleep

print('-='* 20)
print('Analisador de Triângulos v2.0')
print('-=' * 20)
print('Digite três comprimentos para análise.')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('Calculando...')
sleep(1.5)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Deu triângulo!')
    if r1 == r2 == r3: #posso fazer r1 == r2 == r3
        print('Além disso, você formou um triângulo Equilátero!')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1 or r3 == r1 and r3 != r2:
        print('Além disso, você formou um triângulo Isósceles!')
    elif r1 != r2 and r1 != r3 and r2 != r3: # poderia ter usado um else direto e também usado r1 != r2 != r3 != r1
        print('Além disso, você formou um triângulo Escaleno!')
else:
    print('Não deu triângulo. Tente novamente.')
print('--FIM--')