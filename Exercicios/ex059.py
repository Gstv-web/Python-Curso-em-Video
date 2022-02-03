'''
Crie um programa que leia dois valores e mostre um menu na tela:
1- Somar
2- Multiplicar
3- Maior
4- Novos números (digitar novos números de novo)
5- Sair do programa

O programa deverá executar a operação em cada caso.
'''
import openpyxl.worksheet.worksheet

maior = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('Escolha a ação desejada:\n[1] Somar\n[2] Multiplicar\n[3] Mostrar maior número\n[4] Digitar novos números\n[5] Sair do programa\n')
    opcao = int(input('Digite a sua opção: '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    elif opcao == 2:
        print(f'O produto da multiplicação entre {n1} e {n2} é {n1 * n2}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior número é {n1}.')
        elif n2 > n1:
            print(f'Entre {n1} e {n2}, o maior número é {n2}.')
        else:
            print('Ambos números são iguais.')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('--FIM DO PROGRAMA--')
        break
    else:
        print('Digite uma opção válida. Tente novamente.\n')
    print('-=-' * 10)

