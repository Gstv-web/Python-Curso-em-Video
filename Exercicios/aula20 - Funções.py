# Função (def) são rotinas personalizadas, diferente de print(), que já existe no python, por exemplo.
# Bom para criar algo que é será feito constantemente pelo programa.


# Ex. 1
def mensagem(txt): # No exemplo é mensagem, mas não é necessário botar msg, como se fosse algo próprio, é apenas parâmetro.
    print(f'-' * 30)
    print(txt) # parâmetro aqui, quer dizer que é isso que será alterado quando eu chamar a função
    print(f'-' * 30) 

#programa principal
mensagem('Sistema de alunos')
mensagem(' CURSO EM VÍDEO ')
mensagem(' 99999 ')


# Ex. 2
def soma(a, b): # Com mais parâmetros, é necessário colocar todos os parâmetros inseridos, senão dá erro
    s = a + b # A, B e S só receberão valores quando a função for chamada com os parâmetros. 
    print(s)

soma(35, 4)
soma(4+4, 2*4) # posso colocar contas pra somar no final (= 16)
soma(b=50, a=35) # posso explicitar os valores. Caso o faça é necessário fazer com todos os valores, senão dá erro.

# EMPACOTAR PARÂMETROS:
# O * serve pra indicar que diversos parâmetros podem ser jogados diferentemente em diversas funções
# Ex. 3
def contador(* n):
    for valor in n:
        print(f'{valor} ', end='')
    print('FIM')

contador(1, 3, 7, 4) # Tuplas são criadas dessa maneira. Pode-se fazer tudo o que se faz com tuplas
contador(1)
contador(2, 4, 1, 8, 155)

# Ex. 4
# Com listas
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *=2
        pos += 1

valores = [1, 3, 4, 9, 10]
dobra(valores)
print(valores)