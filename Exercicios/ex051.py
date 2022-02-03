# Desenvolva um programa que leia o primeiro termo e a razão de um Progressão Aritmética. No final, mostre os 10
# primeiros termos dessa progressão.
print('=' * 38)
print('PROGRESSÃO ARITMÉTICA')
print('Vou mostrar uma progressão aritmética\nbaseado no primeiro termo e razão')
print('=' * 38)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range (t, t + (10 - 1) * r + r, r): # A própria contagem mostra a progressão, sem "comandos específicos"
    print(f'{c} →', end=' ')
print('ACABOU')