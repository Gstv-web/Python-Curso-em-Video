'''
Faça um programa que mostre a tabuada de vários números - um de cada vez - para cada valor digitado pelo usuário. O pro-
grama será interrompido quando o número solicitado for negativo.
'''

print('-=' * 20)
print('OLHA A TABUADA 3.0')
print('-=' * 20)
c = 0
while True:
    n = int(input('Digite um número para mostrar a tabuada: '))
    print('-' * 20)
    if n < 0:
        break
    while c <= 10:
        print(f'{n:2} x {c:2} = {n * c}')
        c += 1
    c = 0
    print('-' * 20)
print('--FIM--')