r1 = float(input('digite o tamanho da primeira reta:  '))
r2 = float(input('digite o tamanho da segunda reta:   '))
r3 = float(input('digite o tamanho da terceira reta:  '))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print('As retas informadas equivalem a um triangulo')
else:
    print('A retas informadas não equivalem a um triangulo')