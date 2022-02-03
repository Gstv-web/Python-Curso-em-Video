# Um professor quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.
from random import shuffle
alunos = ['Agnes', 'Alex', 'Beatriz', 'Bruno', 'Caio', 'Carol', 'Diego', 'Daniela', 'Emílio', 'Eduarda', 'Fabrício', 'Fabíola', 'Gustavo', 'Guilherme', 'Heitor', 'Janaína', 'Karen', 'Leandro', 'Marta', 'Paloma', 'Sara', 'Thais']
shuffle(alunos)
print(f'A ordem de aprensentação foi definida na seguinte ordem: {alunos}')