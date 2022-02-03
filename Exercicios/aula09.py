# Manipular cadeias de texto -
frase = 'Arroz e Feijão'
print(len(frase))
print(frase.count('o', 0, 11))
print(frase.find('Oloco'))
print('Feijão' in frase)
print(frase.replace('Feijão', 'Ovo'))
print(frase.split())
dividido = frase.split()
print(''.join(dividido))

