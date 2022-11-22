valorC = float(input('Digite o valor do imovel:  '))
salario = float(input('Salario do comprador:   '))
tempo = int(input('Quantidade de anos para pagamento:   '))
ano = 12

parcelas  = valorC / (ano * tempo)

max = salario * 0.30

if parcelas > max:
    print(f'O valor das {parcelas} é superios 30% do salario {salario},Imprestimo foi negado')
else:
    print(f'Suas parcelas em {tempo} ficaram de {parcelas}, Imprestimo foi aprovado')