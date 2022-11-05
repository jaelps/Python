d = float(input('Digite a distacia em Km:   '))

if d <= 200:
    p = d * 0.50

    print(f'O valor da passagem para {d}Km é R$:{p}')
else:
    p2 = d * 0.45

    print(f'O valor da passagem para {d}Km é R$:{p2}')