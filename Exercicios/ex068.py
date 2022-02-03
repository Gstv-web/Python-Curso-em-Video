'''
Faça um programa que jogue par ou ímpar com o usuário. O jogo só será interrompido quando o usuário perder. Após isso,
mostrar na tela quantas vezes consecultivas o usuário venceu.
'''
from random import randint

computador = randint(0,10)
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    parimpar = input('Par ou ímpar? [P/I]: ').upper().strip()
    soma = computador + jogador
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador}, deu PAR')
        if parimpar == 'P':
            print(f'Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    elif soma % 2 != 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador}, deu ÍMPAR')
        if parimpar == 'I':
            print(f'Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
if cont > 1:
    print(f'Você venceu {cont} vezes seguidas.')