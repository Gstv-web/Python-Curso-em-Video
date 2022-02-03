def metade(p, format=False):
    tot = p / 2
    return tot if format is False else moeda(tot)  # Pra não chamar aquele monte de moeda.moeda, essa linha retorna formatado ou não se o parâmetro format for True


def dobro(p, format=False):
    tot = p * 2
    return tot if format is False else moeda(tot)


def aumentar(n, pc, format=False):
    por = n * pc / 100
    tot = n + por
    return tot if format is False else moeda(tot)


def diminuir(n, pc, format=False):
    por = n * pc / 100
    tot = n - por
    return tot if format is False else moeda(tot)


def moeda(p=0, moeda='R$ '):
    return f'{moeda}{p:.2f}'.replace('.', ',')  # Posso usar strings personalizadas sem o comando print!!


def resumo(p, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(p, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(p, taxar, True)}')
    print('-'*30)