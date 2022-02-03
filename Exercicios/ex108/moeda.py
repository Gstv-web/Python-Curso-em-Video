def metade(p = 0):
    tot = p / 2
    return tot


def dobro(p = 0):
    tot = p * 2
    return tot

def aumentar(n = 0, pc = 0):
    por = n * pc / 100
    tot = n + por
    return tot

def diminuir(n = 0, pc = 0):
    por = n * pc / 100
    tot = n - por
    return tot

def moeda(p =0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',') # Posso usar strings personalizadas sem o comando print!!
