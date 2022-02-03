'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção, sem usar o sort().
No final, mostre a lista ordenada na tela.
'''

valores = []

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[len(valores) - 1]: #Se c for o primeiro valor ou n for maior que o último valor
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores): # enquanto pos for menor que o comprimento de valores
            if n <= valores[pos]: # SE n for menor ou igual o VALOR que tem na variável valores, na posição "pos", que é igual a range
                valores.insert(pos, n) # N será inserido na posição X em valores
                break
            pos += 1
print(f'Em ordem: {valores}')