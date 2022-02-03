# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# 1 - binário; 2 - para octal; 3 - hexadecimal

print('-='*20)
print('Conversor de números')
print('-='*20)
numero = int(input('Digite um número para conversão: '))
opçao = int(input('Qual é a base de conversão?\n1 - Binário;\n2 - Octal;\n3 - Hexadecimal;\n'))
if opçao == 1:
    print(f'O resultado é: {bin(numero)[2:]}.')
elif opçao == 2:
    print(f'O resultado é : {oct(numero)[2:]}.')
elif opçao == 3:
    print(f'O resultado é: {hex(numero)[2:]}.')
else:
    print('Digite uma opção válida!')
print('--FIM--')