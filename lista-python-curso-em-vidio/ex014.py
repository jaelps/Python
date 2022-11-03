C = float(input('Digite a temperatura em Cº: '))
F = float(input('Digite a temperatura em Fº:  '))

conversorC = (F - 32)*5/9
conversorF = ((9 * C)/5)+32

print(f'sua temperatura em firerite seria {conversorF:.1f}')
print(f'sua temperatura em celcios seria {conversorC:.1f}')