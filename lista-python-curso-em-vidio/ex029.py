v = float(input('Velocidade do carro em Km/h:  '))


if v <= 80:
    print(f'Sua velocidade é {v}Km/h velocidade esta dentro do limite !!')
else:
    totalM = float(7 * (v - 80))

    print(f'Sua velocidade é {v}Km/h esta acima do permitido, Você foi multado no valor R$:{totalM} por exesso de velocidade!')

print('Tenha um bom dia, Dirija com segurannça !!')

