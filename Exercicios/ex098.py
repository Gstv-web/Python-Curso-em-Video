'''Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e realize a contagem.
O programa tem que realizar três contagens através da função criada
- De 1 até 10, de 1 em 1;
- de 10 até 0, de 2 em 2;
- Uma contagem personalizada.'''

from time import sleep

''' DUAS FUNÇÕES COM FOR - PURA TRAPAÇA, MAS FUNCIONA
def contadormais(a, b, c): # Função pra contagem progressiva
    print('-=' * 40)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for cont in range(a, b+1, c):
        print(f'{cont}', end=' ')         
        sleep(0.30)
    print('- Fim da contagem')

def contadormenos(a, b, c): # Função pra contagem regressiva
    print('-' * 40)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for cont in range(a, b-1, -c):
        print(f'{cont}', end=' ')
        sleep(0.35)
    print('- Fim da contagem')


contadormais(1, 10, 1)
contadormenos(10, 0, 2)
'''
def contador(a, b, c):
    print('-' * 40)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    cont = a
    if a < b:
        while cont <= b:
            print(f'{cont}', end=' ')
            cont += c
            sleep(0.35)
        print('- Fim da contagem')
    else:
        while cont >= b:
            print(f'{cont}', end=' ')
            cont -= c    
            sleep(0.35)
        print('- Fim da contagem')

contador(1, 10, 1)
contador(20, 0, 2)
print('Agora é sua vez de personalizar a contagem.')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
if c < 0: # Condicional pra se mesmo se eu colocar número negativo, mostrar como positivo e ainda assim fazer a contagem regressiva
    c *= -1
if c == 0: # Se o passo for 0, ele vai valer 1
    c = 1
contador(a, b, c)

''' PARA A VERSÃO COM FOR
if c < 0: # Condicional pra se mesmo se eu colocar número negativo, mostrar como positivo e ainda assim fazer a contagem regressiva
    c *= -1
if c == 0: # Se o passo for 0, ele vai valer 1
    c = 1    
if a > b:
    contadormenos(a, b, c)
else:
    contadormais(a, b, c)
    '''