# Laços com for

# for c in range (301, -1) É possível fazer contagens ao contrário

for c in range(0, 301, 2): # Ou no caso, a terceira opção é de como será contado
    print(c)
print('--FIM--')

'''n = int(input('Digite um número: '))
for c in range(0,n+1): # Posso usar uma váriável como limite ou começo
    print(c)
print('--FIM--')'''

'''i = int(input('Início:'))
f = int(input('Fim: '))
p = int(input('Passo:'))
for c in range(i, f+1, p): #É possível usar a range das variáveis
    print(c)
print('--FIM--')'''

'''s = 0
for c in range(0,5):
    n = int(input('Digite um número: ')) # Esse comando irá se repetir
    s += n # faz a soma com o último número digitado
print(f'A soma dos números é igual a {s}')'''