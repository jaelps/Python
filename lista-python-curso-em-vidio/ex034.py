nome = str(input('Nome do funcionario:  '))
salario = float(input('Valor do salario:  '))

s = 1250
al1 = (salario * 0.10) + salario
al2 = (salario * 0.15) + salario

if salario >= s:
    print(f'Funcionario {nome} seu salario é {salario}, você tem direto a um almeto de 10% você vai reseber R$:{al1}')
else:
    print(f'Funcionario {nome} seu salario é {salario}, você te direto a um almento de 15% e vai receber R$:{al2}')
