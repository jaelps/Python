r1 = float(input('digite o tamanho da primeira reta:  '))
r2 = float(input('digite o tamanho da segunda reta:   '))
r3 = float(input('digite o tamanho da terceira reta:  '))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:

    if r1 == r2 == r3 and r2 == r3 == r1 and r3 == r1 == r2:
        print(f'As retas formam um trinagolo EQUILÁTERO')
    elif r1 == r2 != r3 and r2 == r3 != r1 and r3 == r1 != r2:
        print(f'As retas formam um triangolo ISÓSCELES')
    elif r1 != r2 != r3 and r3 != r2 != r1 and r3 != r1 != r2:
        print(f'As retas formam um triangolo ESCALENO')

else:
    print('As teras informadas não formão um triangolo')