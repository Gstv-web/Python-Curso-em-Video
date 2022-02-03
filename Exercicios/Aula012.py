# Condições aninhadas if... elif.... else

nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo!')
elif nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Agnes Laura':
    print('Belo nome feminino!')
else:
    print('Seu nome é comum.')
print(f'Tenha um bom dia, {nome}!')
