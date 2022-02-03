# Desenolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem , cobrando  R$ 0,50
# por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

# Perguntar a distancia (em Km) do destino

from time import sleep

dist = float(input('Digite a distância do destino: '))
print(f'Calculando valor para {dist}Km...')
sleep(1.5)

# Calcular o preço por km. 0,50 até 200km, 0,45 pra mais de 200km

if dist <= 200:
    pr = dist * 0.50
    print(f'O preço total da viagem será de R$ {pr:.2f}.')
else:
    pr = dist * 0.45 # Aparentemente posso usar a mesma variável, uma vez que a condição da mesma mudaria.
    print(f'O preço total da viagem será de R$ {pr:.2f}.')