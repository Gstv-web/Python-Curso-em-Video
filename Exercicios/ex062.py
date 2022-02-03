# PA da aula 61 melhorada

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
ntermo = 10
while ntermo != 0:
    total = total + ntermo
    while cont <= total:
        print(f'{termo}', end=' → ')
        termo += razão
        cont += 1
    print('PAUSA\n')
    ntermo = int(input('Deseja ver mais termos? Digite a quantidade: '))
print('FIM')
print(f'No total foram mostrados {total} termos')
