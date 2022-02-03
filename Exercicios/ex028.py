"""
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pela máquina. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

# FAZER A MÁQUINA PENSAR EM UM NÚMERO ENTRE 0 E 5

import random
from time import sleep

computador = random.randint(0, 1) # randint já gera um número com os parâmetros sem precisar fazer uma lista

# PEDIR PARA O USUÁRIO DIGITAR UM NÚMERO

escolha = int(input('Eu escolhi um número entre 0 e 5. Duvido você adivinhar qual é! Digite o número: '))
print('Processando...')
sleep(3) # Função bacana

# MOSTRAR NA TELA SE ACERTOU OU ERROU

if escolha == computador:
    print('Droga, você acertou! >:(')
else:
    print('HAHAHA! Você errou!')
print('--FIM--')