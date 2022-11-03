import random

nome1 = str(input('Nome aluno: '))
nome2 = str(input('Nome aluno: '))
nome3 = str(input('Nome aluno: '))
nome4 = str(input('Nome aluno:  '))

list = [nome1, nome2, nome3, nome4]

random.shuffle(list)

print('A ordem de alunos é')
print(list)