'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os numa tupla. No final, mostre:
- Quantas vezes apareceu o valor 9;
- Em que posição foi digitado o primeiro valor 3;
- Quais foram os números pares.
'''



n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Os números digitados foram: ', end='')
for c in n:
    print(c, end=' ')
if 9 in n: # "Se há o número 9 em n
    print(f'\nO número 9 apareceu {n.count(9)} vez(es).') # var.count() mostra quantas vezes o valor escolhido na variável aparece  dentro da mesma.
else:
    print('\nO valor 9 não foi digitado.')
if 3 in n:
    print(f'O primeiro número 3 foi digitado na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'Os números pares digitados foram: ', end='')
for par in n:
    if par % 2 == 0:
        print(f'{par}', end=' ')