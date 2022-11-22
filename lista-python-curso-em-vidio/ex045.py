import random
print('''Suas opções:
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura''')
opcao = int(input('Qual a sua jogada?   '))




list = ['Pedra', 'Papel', 'Tesoura']
jogada = random.choice(list)


if opcao == 0 :
    print(f'Computador jogou {jogada}')
    print('Jogador jogou Pedra')
    
    if jogada == 'Pedra':
        print('EMPATE')

    elif jogada == 'Papel':
        print('VOCÊ PERDEU')

    elif jogada == 'Tesoura':
        print('VOCÊ VENCEU')

elif opcao == 1:
    print(f'Computador jogou {jogada}')
    print('Jogador jogou Papel')

    if jogada == 'Papel':
        print('EMPATE')

    elif jogada == 'Pedra':
        print('VOCÊ VENCEU')

    elif jogada == 'Tesoura':
        print('VOCÊ PERDEU')

elif opcao == 2:
    print(f'Computador jogou {jogada}')
    print('Jogador jogou Tesoura')

    if jogada == 'Tesoura':
        print('EMPATE')

    elif jogada == 'Papel':
        print('VOCÊ VENCEU')
        
    elif jogada == 'Pedra':
        print('VOCÊ PERDEU')

else:
    print('Erro')


