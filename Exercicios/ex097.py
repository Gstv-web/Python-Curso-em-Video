'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostra uma mensagem com tamanho adaptável'''

def escreva(txt):
    tam = len(txt) #crio uma variável que pega o tamanho do que for escrito.
    print('~' * tam)
    print(txt)
    print('~' * tam)


escreva('Gustavo')
escreva('Vamos ver se deu certo')
escreva('Deu?')