# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal , sabendo que ela
# não pode exceder 30% do seu salário ou então o empréstimo será negado.

# Ler o valor do imóvel, salário e anos para pagamento

from time import sleep
print('-='*20)
print('Verificador de Emprestimos®')
print('-='*20)
imovel = float(input('Digite o valor do imóvel: R$ '))
sal = float(input('Digite o salário do comprador: R$ '))
a = int(input('Digite o número de prestações (em anos): '))
anos = a * 12
prestacao = imovel / anos
max = sal * 30 / 100

print('Calculando valor e prestações...')
sleep(1.8)
print(f'{anos} vezes de R$ {prestacao:.2f}')
if prestacao >= sal * 30 / 100:
    print('Empréstimo não aprovado. Valor da parcela ultrapassa 30% do salário do comprador.')
else:
    print(f'Empréstimo aprovado! O valor será de {prestacao:.2f} em {anos} prestações.')