# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo

from time import sleep
print('-='*35)
print('Será que vai dar triângulo? Digite o comprimento das retas.')
print('-='*35)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

print('Calculando...')
sleep(0.5)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Deu triângulo!')
else:
    print('Não deu triângulo :(')
print('--FIM--')