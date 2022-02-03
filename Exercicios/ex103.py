'''Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais: o NOME de um jogador e quantos GOLS ele marcou.
O programa deverá ser capaz de mostrar a ficja do jogador. mesmo que algum dado não tenha sido informado corretamente'''

def ficha(nome='<desconhecido>', g=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    
# Main
jogador = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric(): # int não pode não ter valor, então pra driblar, converte-se o str pra int
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(g=gols)
else:
    ficha(jogador, gols)