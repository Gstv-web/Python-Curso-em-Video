nota1 = float(input('Nota do primeiro bimestre: '))
nota2 = float(input('Nota do segundo bimestre: '))
nota3 = float(input('Nota do terceiro bimestre: '))
nota4 = float(input('Nota do quarto bimestre: '))
total = (nota1 + nota2 + nota3 + nota4) / 4
if total >= 7:
    print(f'A nota final foi {total:.1f}. Aprovado.')
elif total >= 6:
    print(f'A nota final foi {total:.1f}. Poderá fazer a recuperação.')
else:
    print(f'A nota final foi {total:.1f}. Reprovado.')
print('--FIM--')

#Fiz um elif só pra ver, funfou.