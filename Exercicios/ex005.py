# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SEU SUCESSOR E SEU ANTECESSOR
n1 = int(input('Digite um número: '))
n2 = 1
print('Você digitou o número {}'.format(n1))
print('O número anterior a {} é {}'.format(n1, n1-n2))
print('O número depois de {} é {}'.format(n1, n1+n2))
# CORRIGIDO, MAS FUNCIONOU. ENTRETANTO, POSSO USAR SOMENTE UMA VARIÁVEL, no format é só botar o calculo da variavel