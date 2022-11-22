n1 = float(input('Digite a nota do primerio bimestre: '))
n2 = float(input('Digite a nota o segundo bimestre:   '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'sua media foi {media}, você foi REPROVADO')
elif media == 5.0 and media < 6.9:
    print(f'sua media foi {media}, você esta na RECUPERAÇÃO')
else:
    print(f'sua media foi {media}, você foi APROVADO')