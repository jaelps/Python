print('Verificação de idade')

ef = '-=-' *30
print(ef)

ano = int(input('Qual ano que você nasceu ??'))

print(ef)

idade = (ano - 2022)* -1
t = (idade - 18) * -1

if idade <= 18:
    print(f'Você ainda vai se alista no serviço militar, da em {t} anos')
elif idade == 18:
    print('Esta na hora de se alistar no seviço militar')
else:
    print(f'Já passou, {t} anos o tempo de alistamento')



