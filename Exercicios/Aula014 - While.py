# Laços com While
# While cria laços indeterminadamente
'''
c = 1
while c < 10:
    print(c) # é preciso criar uma variável "contadora"
    c += 1
print('--FIM--')
'''


# Posso criar pontos de parada (enquanto eu digitar S, sempre vai pedir um número)
'''r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? ')).upper()
print('--FIM--')


'''
n = 1
par = impar = 0
while n != 0: # ponto de parada
    n = int(input('Digite um número: '))
    if n != 0: # para o 0 não contar como par
        if n % 2 == 0 and n != 0:
            par += 1
        else:
            impar +=1
print('Acabou!')
print(f'Foram digitados {par} números pares e {impar} números ímpares.')