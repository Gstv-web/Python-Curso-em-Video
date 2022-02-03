'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
maior = 0

dados = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)
}
ranking = {} # Precisei criar outro dicionário pra então poder ordenar os dados
print('Valores sorteados:')
for p, d in dados.items():
    sleep(0.75)
    print(f'{p} tirou {d}')
print('Ranking dos jogadores:')
ranking = sorted(dados.items(), key=itemgetter(1))
ranking.reverse()
for i, v in enumerate(ranking):
    sleep(0.75)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')