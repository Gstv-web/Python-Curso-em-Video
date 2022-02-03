# Faça um programa que mostre na tela uma contagem regressiva indo de 10 até 0 com delay de 1s

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('**FOGOS**')