# Crie um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

final = []
for p in range(1,6):
    peso = final.append(float(input(f'Digite o peso da {p}ª pessoa: ')))
print(f'O peso mínimo identificado foi {min(float(p) for p in final)}Kg e o peso máximo identificado foi {max(float(p) for p in final)}Kg')