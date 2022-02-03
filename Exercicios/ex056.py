''' Escreva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
- A média de idade do grupo;
- O nome do homem mais velho;
- Quantas mulheres tem menos de 20 anos.
'''


print('Analisador Complexo')

c = 0
idademais = 0
idademenos = 0
nomehomem = ''
for d in range(1, 5):
    print(f'---- {d}ª PESSOA ----')
    n = str(input(f'Nome: ')).strip()
    i = int(input(f'Idade: '))
    s = input(f'Sexo [M/F]: ').strip()
    c += i
    if d == 1  and s in 'Mm': # se o contador for igual a 1 e tiver Mm em s
        idademais = i # variavel recebe i
        nomehomem = n # variável recebe n
    if s in 'Mm' and i > idademais: # Mas também tem que ver se há Mm em s e se i > variavel, se sim
        idademais = i # variável recebe nova i
        nomehomem = n
    else:
        if i < 20 and s in 'Ff':
            idademenos += 1
print(f'A média de idade do grupo é de {c / 4} anos.')
print(f"O homem mais velho possui {idademais} anos e se chama {nomehomem}.")
print(f'Ao todo, temos {idademenos} mulhere(s) com menos de 20 anos.')