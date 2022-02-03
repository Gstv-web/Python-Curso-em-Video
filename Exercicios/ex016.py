#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA SUA PORÇAO INTEIRA
import math
n = float(input('Digite um número qualquer: '))
print(f'O número {n} tem a parte inteira {math.trunc(n)}')