''' Crie um programa que tenha uma função chamada fatoriaç() que receba dois parâmetros: um número a calcular e outro chamado show, que será um valor lógico(opcional) indicando
se serpa mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(num, show=False): # No caso, o show serve pra mostrar ou esconder os prints dentro da função, mostrando somente o valor do return
    """-> Calcula o fatorial de um numero

    Args:
        num: Número a ser calculado
        show: Mostrar ou não a conta. Defaults to False.

    Returns:
        O valor do fatorial de um número n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f

help(fatorial)