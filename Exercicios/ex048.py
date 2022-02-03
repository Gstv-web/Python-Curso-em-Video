# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 que se encontram no
# intervalo entre 1 e 500

s = 0
cont = 0
for impar3 in range(1, 501):
    if impar3 % 3 == 0 and impar3 % 2 != 0:
        cont += 1 # contador
        s += impar3 # acumulador
print(f'A soma de todos os {cont} números ímpares múltiplos de 3 é {s}')