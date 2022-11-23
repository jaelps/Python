somaidade = 0
mediaidade = 0
maioridadeM = 0
maisvelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'------{p}ª pessoa-----------')
    nome = str(input('Digite o nome:  ')).strip()
    idade = int(input('Digite a idade:   '))
    sexo = str(input('sexo: [M/F]')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadeM = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridadeM:
        maioridadeM = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é {mediaidade} anos')
print(f'o homem mais velho se chama {maisvelho} e tem {maioridadeM} idade')
print(f'ao todo são {totmulher20} com menos de 20 anos ')
