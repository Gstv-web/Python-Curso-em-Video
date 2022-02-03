'''
Crie um programa que leia uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
if n < 0 or n > 20:
    n = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[n]}')