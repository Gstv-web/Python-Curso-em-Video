# ---Funções---

# Interactive Help

# help()


# Docstrings - manuais de uma função (pra entender o que é) *** Importante ***
def contador(i, f, p=2):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

contador(1, 10,)

# Parâmetros opcionais
# Exemplo de somar(a, b, c) - Neste caso é necessário discriminar os três parâmetros, senão o programa vai dar erro.
# Agora, somar(a, b, c=0) - Neste caso, eu posso chamar uma função somar(21, 4), onde 'c=0', ou seja, ele tem esse valor já atribuído, podendo ser sem problema somar(a=0, b=0, c=0)
# Posso atribuir parâmetros fora de ordem também.



# Escopo de variáveis - Local onde uma variável vai existir ou não
# uma variável criada dentro de uma função, por exemplo, só irá ser lida naquela função, loop, etc. Se ela estiver fora, ela poderá ser lida de onde for, desde que seja atribuída
# antes de ser lida.
# dentro de uma função, posso digitar global v (v = variável), onde a variável global será usada ao invés de criar uma variável local de mesmo nome, porém posso dar um novo valor dentro
# do escopo


 
# Retorno de Valores
# return

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # flexibiliza o uso de resultados

r1 = somar(2, 2, 2)
r2 = somar(10, 25, 5)
r3 = somar(4, 8)

print(f'Usando um return s, posso mostrar os resultados da função em variáveis, por exemplo {r1}(r1 = somar(2, 2, 2), {r2} (r2 = somar(10, 25, 5) e {r3} (r3 = somar(4, 8)')
