# Tuplas são variáveis compostas
# TUPLAS SÃO IMUTÁVEIS, ou seja, não é possível alterar o que tá dentro da tupla enquanto está executando.

lanche = ('Hamburger', 'Milk Shake', 'Fritas', 'Pudim')
print(lanche)

#for c in lanche:
#    print(c)

for comida in range(0, len(lanche)):
    print(lanche[comida])

for pos, comida in enumerate(lanche):
    print(f'{comida} está na posição {pos}')

print(sorted(lanche)) #bota em ordem, mas não altera

a = 1, 3, 4
b = 7, 6, 9, 3
print(a, b) #Se eu botasse b primeiro, b aparece primeiro

pessoa = ('Gustavo', 29, 75, 1.78) # posso usar dados diferentes dentro das tuplas
print(f'O nome da pessoa é {pessoa[0]}, sua idade é {pessoa[1]}, pesa {pessoa[2]}Kg e mede {pessoa[3]}m')