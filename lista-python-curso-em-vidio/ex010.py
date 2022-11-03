nome = str(input('Qual seu nome?   '))
saldo = float(input('Quanto você tem na carteira: '))

dolar1 = 5.14
conversao = saldo / dolar1

print(f'O Clinete {nome} tem R$:{saldo} em sua carteira, com este valor você pode comprar ${conversao:.2f} dolares')
