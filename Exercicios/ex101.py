'''Crie um programa que tenha uma função voto() que vai receber como parâmetro o ANO DE NASCIMENTO de uma pessoa, retornando um valor literal (frase, palavra) indicando se uma pessoa tem
voto negado, obrigatório ou opcional nas eleições'''

from datetime import date

def voto(a):
    nvota = f'COM {data} anos: NÃO VOTA'
    obrig = f'Com {data} anos: VOTO OBRIGATÓRIO'
    opcional = f'Com {data} anos: VOTO OPCIONAL'
    if data >= 65:
        return opcional # return faz voltar uma váriável, portanto não preciso fazer código fora da função
    if data >= 18:
        return obrig
    if data >= 16:
        return opcional
    else:
        return nvota


# Main
ano = int(input('Em que ano você nasceu? '))
data = date.today().year - ano
print(voto(data))