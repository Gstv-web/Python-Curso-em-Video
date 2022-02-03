'''Exercício 93 aprimorado para que funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador'''


jogador = dict()
partidas = list()
time = list()

while True: # Pedir nome de jogador, partidas jogadas e gols por partida
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(1, tot+1): # em x partidas
        partidas.append(int(input(f'Quantos gols foram feitos na partida {c}: '))) # É possível dar append direto com inserção de dados na variável
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja adicionar outro jogador? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO - Digite apenas S ou N.')
    if resp == 'N':
        break # fim do código
print('=--=' * 15)
print('cod ', end='') # mostrar o cabeçalho com as keys do dicionário jogador
for i in jogador.keys():
    print(f'{i:<18} ', end='')
print() # fim do código
print('-' * 60)
for i, j in enumerate(time): # i = key, j = value - Mostrar (enumerado) as keys da lista time e os valores (nome, gols de cada partida e total de gols)
    print(f'{i:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<18} ', end='')
    print() # fim do código
print('=--=' * 15)
while True: # levandar dados de um jogador específico da lista depois da leitura
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO - Não existe jogador com código {busca}. Tente novamente.')
    else:
        print(f'-- Levantamento do jogador {time[busca]["nome"]}:') # time é a lista, busca é um dos index (len(time)) e como é um dicionário dentro da lista, g pega o value de ["nome"] 
        for j, g in enumerate(time[busca]['gols']): # mesma ideia acima
            print(f'No jogo {j+1}, ele fez {g} gol(s).')
print('--FIM DO PROGRAMA--')
    