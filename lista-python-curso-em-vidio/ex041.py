from datetime import date

nasc = int(input('Ano de Nascimento:   '))
idade = date.today().year - nasc

if idade < 9:
    print(f'sua idade é {idade}, você esta na categoria MIRIN')
elif idade <= 14:
    print(f'sua idade é {idade}, sua caregoria é INFANTIL')
elif idade <= 19:
    print(f'sua idade é {idade}, você esta na catergoria JUNIOR')
elif idade <= 25:
    print(f'sua idade é {idade}, você esta na categoria SENHOR')
else:
    print(f'sua idade é {idade}, você esta na categoria MASTER')