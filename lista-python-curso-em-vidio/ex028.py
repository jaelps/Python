import random

list = [0,1,2,3,4,5]
sorteio = (int(random.choice(list)))

#computador = randint(0, 5) # faz o computador penças em um numero

numero = int(input('Digite um numero:  '))

if numero == sorteio:
    print(f'O nome escolhido foi {sorteio}, você escolheu {numero}, parabens você acertou !!!')
else:
    print(f'O nome escolhido foi {sorteio}, você escolheu {numero}, você errou :(')

    #não funcional