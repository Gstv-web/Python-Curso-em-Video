# Melhore o desafio 28 onde o computador vai "pensa" em um número entre 0 a 10. Só que agora errando, o jogador continuará
# jogando até acertar. No final mostrar o número de tentativas

from random import randint

'''
print('-=' * 30)
print('O JOGO DA ADIVINHAÇÃO')
print('-=' * 30)
jogador = int(input('Escolhi um número entre 0 e 5. Duvido você adivinhar! Digite o número: '))
maquina = randint(0, 5)
tentativas = 0
while jogador != maquina:
    jogador = int(input('HAHAHA! Você errou! Tente novamente: '))
    maquina = randint(0, 5)
    tentativas += 1
if tentativas == 0:
    print('Caraio, mano! Você acertou de primeira, seu hacker!')
if tentativas < 5:
    print(f'Rapaz, cê é bom mesmo! Só precisou de {tentativas} tentativas. Mas acho que foi sorte!')
if tentativas >= 5:
    print(f'Droga! você venceu. Porém, você tentou {tentativas} vezes até conseguir')'''

maquina = randint(1, 5)
print(maquina)