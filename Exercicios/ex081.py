'''
Crie um programa que leia vários números e colocar e uma lista. Depois, mostre:
- QUANTOS números foram digitados;
- A lista de valores em ordem decrescente;
- Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []
resp = 'S'
while resp == 'S':
    n = int(input('Digite um número: '))
    valores.append(n)
    resp = input('Deseja continuar? S/N: ').upper()
print(f'Você digitou {len(valores)} números.')
valores.sort(reverse=True) # Tenho que dar um print depois disso, senão não vai
print(f'Os números digitados em ordem descrescente é a seguinte: {valores}')
if 5 in valores:
    print(f'O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')