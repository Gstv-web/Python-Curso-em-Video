'''Crie um programa que leia o nome de um jogador de futebol e que peça para colocar quantos gols foram feitos em X partidas. Depois, mostrar na tela a quantidade de gols
na partida e o número total de gols'''

dados = dict()
# Pedir o nome do jogador
dados['jogador'] = str(input('Digite o nome do jogador: '))
# Pedir para colocar quantos gols foram feitos por partida em x delas
match = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
dados['gols'] = []
tot = 0
for p in range(1, match+1):
    partida = int(input(f'Quantos gols foram feitos na partida {p}: '))
    tot += partida
    dados['gols'].append(partida)
dados['total'] = tot
print(dados)
print('=--=' * 15)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=-=' * 15)
print(f'O jogador {dados["jogador"]} jogou {p} partidas.')
for i, g in enumerate(dados['gols']):
        print(f'=> Na partida {i+1} ele marcou {g} gol(s).')
print(f'O jogador fez um total de {tot} gols.')