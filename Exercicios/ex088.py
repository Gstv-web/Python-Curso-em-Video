'''Faça um progama que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta'''

from random import randint
from time import sleep
temp = []
jogos = []
jogos.sort()
print('-' * 30)
print('MEGA SENA ALEATÓRIA')
print('-' * 30)
quant = int(input('Digite a quantidade de jogos que você quer gerar: ')) + 1
cont = 1
for j in range(0, quant):
    for n in range(1, 7):
        num = (randint(1, 60))
        if num not in temp:
            temp.append(num)
    jogos.append(temp[:])
    temp.clear()
print(f'-=-=-=- SORTEANDO {quant - 1 } JOGO(S) -=-=-=-')

for j in range(1, quant):
    jogos[j].sort()
    print(f'JOGO {cont}: {jogos[j]}')
    cont += 1
    sleep(0.5)
print(f'{"-=-=-=-     BOA SORTE!     -=-=-=-":40}')