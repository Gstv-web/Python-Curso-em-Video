# Desenvolva um programa que leia o primeiro termo e a razão de um Progressão Aritmética. No final, mostre os 10
# primeiros termos dessa progressão COM WHILE

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print(f'{t + (c - 1) * r} → ', end='')
    c += 1
print('FIM')