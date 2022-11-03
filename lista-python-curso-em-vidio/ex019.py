import random

nome1 = str(input('Nome do primero aluno:  '))
nome2 = str(input('Nome do segundo aluno:  '))
nome3 = str(input('Nome do terceiro aluno:  '))
nome4 = str(input('Nome do quarto anuno:   '))

list = [nome1, nome2, nome3, nome4]

sorteio = random.choice(list)

print(f'O aluno da vez é {sorteio}')



