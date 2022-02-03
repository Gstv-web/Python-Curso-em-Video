tempo = int(input('Quantos anos seu carro tem? '))
if tempo <= 3:
    print('Seu carro tá novinho! Ainda não desvalorizou!')
else:
    print('Seu carro já está desvalorizado.')
print('--FIM--')

# Posso fazer a mesma coisa acima em uma única linha:
# print('Seu carro tá novinho![...] if tempo <= 3 else 'Seu carro[...]')