n1 = int(input('Primeiro numero:  '))
n2 = int(input('Segundo numero:   '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>>>>Qual é a sua opção?  '))
    if opcao == 1:
        soma = n1 + n2
        print(f' a soma de {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplica = n1 *n2
        print(f'a multiplicação de {n1} x {n2} é igual a {multiplica}')
    elif opcao  == 3:
        if n1 > n2:
            maior = n1
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            maior = n2
            print(f'{n2} é maior que {n1}')
        elif n1 == n2:
            print(f'os numeros {n1} e {n2} são iguais')

    elif opcao == 4:
        print('informe novos numeros')
        n1 = int(input('primeiro numero: '))
        n2 = int(input('segundo numero: '))
    elif opcao == 5:
        print('finalizado')
    else:
        print('opcão invalida tente de novo')
print('Você saio do programa')