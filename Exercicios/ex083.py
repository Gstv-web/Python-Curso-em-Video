'''Crie um programa que leia uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta'''

expr = str(input('Digite uma expressão matemática: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(') # Se simb for (, adiciona ( na pilha
    elif simb == ')':
        if len(pilha) > 0: # Se comprimento da pilha for maior que 0
            pilha.pop() # Tira a última variável
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
print(pilha)