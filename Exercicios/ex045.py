# Faça um jogo de jokenpô
# RANDINT CORTARIA MUITA LINHA, mas funcionou mesmo assim
import random
from time import sleep

arma = ['pedra', 'papel', 'tesoura']
jogador = str(input(f'Escolha entre {arma}'))
computador = random.choice(arma)

if jogador == 'pedra':
    print(f'*Você escolheu {arma[0]}*')
elif jogador == 'papel':
    print(f'*Você escolheu {arma[1]}*')
else:
    print(f'*Você escolheu {arma[2]}*')
sleep(1)
print('Estou escolhendo o meu...')
sleep(1)
print('Vamos lá?')
sleep(1)
print('JO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PÔ!')
print(f'Eu escolhi {computador}')
if jogador == 'pedra' and computador == 'pedra' or jogador == 'papel' and computador == 'papel' or jogador == 'tesoura' and computador == 'tesoura':
    print('AH! Houve um empate! Vamos de novo!')
elif jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel':
    print('DROGA, você ganhou! Não vou perder a próxima.')
else:
    print('HAHAHA! Você perdeu!')
print('--FIM--')