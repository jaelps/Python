primeriro = int(input('primerio termo:  '))
razao = int(input('razão:  '))
decimo = primeriro + (10 - 1) * razao
for i in range(primeriro, decimo, razao):
    print(f'{i}', end='->')
print('Acabou')