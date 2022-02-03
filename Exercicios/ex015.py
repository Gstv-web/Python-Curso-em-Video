#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS
# ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR SABENDO QUE O CARRO CUSTA R$ 60,00/DIA E R$0,15/KM.
dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('QUantos Km foram percorridos? '))
d = 60 * dia
k = 0.15 * km
print(f'O valor das diárias equivalem a R$ {d:.2f}.')
print(f'O valor da kilometragem equivale a R$ {k:.2f}.')
print(f'Valor a ser pago: R$ {d + k:.2f}')