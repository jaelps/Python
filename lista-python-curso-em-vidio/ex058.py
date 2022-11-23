from random import randint
computador = randint(0,10)
print('sou seu computador vou pençar em u numero 0 a 10')
print('adivinhe se puder!!!')
acertou = False
papite = 0
while not acertou:
    jogador = int(input('tente de novo:  '))
    papite = papite +1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... tente de novo !')
        elif jogador > computador:
            print('Menos... tente de novo!')
print(f'acertou com {papite} palpites')