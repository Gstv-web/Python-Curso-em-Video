#UM PROFESSOR QUER SORTEAR QUATRO ALUNOS PARA LIMPAR A LOUSA. FAÇA UM PROGRAMA  QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME ESCOLHIDO
#AQUI EU FIZ DIFERENTE, MAS DEU CERTO (ESCOLHEU SOMENTE 1, MAS A IDEIA DO RANDOM FOI)
import random
alunos = ['Agnes', 'Alex', 'Beatriz', 'Bruno', 'Caio', 'Carol', 'Diego', 'Daniela', 'Emílio', 'Eduarda', 'Fabrício', 'Fabíola', 'Gustavo', 'Guilherme', 'Heitor', 'Janaína', 'Karen', 'Leandro', 'Marta', 'Paloma', 'Sara', 'Thais']
print(f'O aluno escolhido foi: {random.choice(alunos)}')