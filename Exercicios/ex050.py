# Desenvolva um programa que leia seis números inteiros e mostre a soma somente dos números pares. Se o valor for ímpar,
# desconsidere-o.

print('Digite seis números para somá-los.')
s = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'A soma dos {cont} números pares identificados é de {s}')