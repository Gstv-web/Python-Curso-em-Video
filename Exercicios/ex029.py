# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre  uma mensagem dizendo que foi
# multado. A multa vai custar R$ 7,00 pra cada km acima do limite

# Ler a velocidade do carro

from time import sleep


velocidade = int(input('Velocidade do veículo: '))
print('Lendo...')
sleep(2)
print(f'A velocidade é de {velocidade}Km/h.')

# Dar multa pra cada km a mais acima de 80

if velocidade <= 80:
    print('--FIM--')
else:
    print('MULTADO! O veículo está acima do permitido.')
    print('Calculando multa...')
    sleep(2)
    multa = (velocidade % 80) * 7 # Posso criar variável dentro do bloco que tá suave
    print(f'Total a pagar: R${multa:.2f}.')
    print('--FIM--')
# Nenhuma ação se estiver no limite