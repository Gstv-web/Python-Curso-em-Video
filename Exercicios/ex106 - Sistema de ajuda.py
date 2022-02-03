'''Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará'''

from time import sleep

c = ('\033[m',          # 0 - Sem cores
    '\033[0;30;41m',     # 1 - Vermelho
     '\033[7m',      # 2 - Invertido
     '\033[1;1;107m',      # 3 - Branco
     '\033[1;47m'       # 4 - Cinza claro
    )

def ajuda(com, cor=0): # POSSO CHAMAR UMA FUNÇÃO DENTRO DE OUTRA FUNÇÃO
    titulo(f'Acessando o manual do comando "{comando}"', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(0.65)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')

# Main
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!!!', 1)
        break
    else:
        sleep(0.50)
        ajuda(comando)