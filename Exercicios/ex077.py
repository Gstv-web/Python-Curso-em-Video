'''
Crie um programa que tenha uma tupla com várias palavras (sem acento). Depois disso, mostre para cada plavara quais são
as suas vogais
'''


palavras = ('Arroz', 'Queijo', 'Fruta', 'Macarrao', 'Salada', 'Bacon', 'Amendoim', 'Banana', 'Coxinha', 'Manjericao',
            'Pimenta', 'Lagosta', 'Pizza', 'Ovo')
for p in palavras:
        print(f'\nNa palavra {p.upper()} temos ', end='')
        for letra in p: # mesmo numa tupla, strings são LISTAS de letras, portanto posso procurar por letras dentro das palavras de uma tupla
            if letra.lower() in 'aeiou':
                print(letra, end=' ')