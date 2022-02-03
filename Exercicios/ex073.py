'''Crie uma tupla com os times do brasileirão, na ordem de colocação. Depois mostre:
- Apenas os 5 primeiros colocados;
- Os últimos 4 colocados na tabela:
- Uma lista com os times em ordem alfabética;
- Em que posição está o time do Santos.'''

times = ('Internacional', 'São Paulo', 'Atlético-MG', 'Vasco da Gama', 'Fluminense', 'Flamengo', 'Ceará SC', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Santos', 'Bahia', 'Atlético-PR', 'Sport Recife', 'Coritiba', 'Grêmio', 'Botafogo', 'Bragantino-SP', 'Atlético-GO', 'Goiás')
alvo = 'Santos'
print('=' * 40)
print(f'Lista de times Brasileirão 2020: {times}')
print('=' * 40)
print(f'Os cinco primeiros colocados são: {times[:5]}')
print('=' * 40)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('=' * 40)
print(f'A lista do Brasileirão em ordem alfabética fica da seguinte maneira: {sorted(times)}')
print('=' * 40)
print(f'O Santos está na {times.index("Santos")}ª posição.') # index faz eu procurar em qual len está o que eu digitar