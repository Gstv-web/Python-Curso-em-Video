# RETORNO DE VARIÁVEIS - Posso devolver listas, dicionários, tuplas, uma porrada de coisa
# EXEMPLOS
# 1
def fatorial(num=1): # parâmetro opcional
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

# 2

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(2)

print(f'Os resultados são {f1} {f2} {f3}')

# 3

def par(n=0):
    if n%2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(f'Retornando {par(num)} por conta do return True ou False na função ') # mostra a chamada da função par da variável num
if par(num):
    print('É par.')
else:
    print('É ímpar.')