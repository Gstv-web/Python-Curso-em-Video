'''Desenvolva unma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a
tabela:
- Abaixo de 18.5: Abaixo do Peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida
 '''

print('-=' * 20)
print('Calculdadora de IMC')
print('-=' * 20 )

alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está com peso abaixo do normal.')
elif imc <= 24.9:
    print(f'Seu IMC é {imc:.1f}. Você está com peso ideal.')
elif imc <= 29.9:
    print(f'Seu IMC é {imc:.1f}. Você está com sobrepeso.')
elif imc <= 39.9:
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade.')
else:
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade mórbida.')
print('--FIM--')