nome = str(input('Nome do funcionario: '))
salario = float(input('Valor do salario: '))
aumento = 0.15
#salario + (salario* 15 /100)

total = salario * aumento
total2 = total + salario

print(f'O funcionario {nome} resebe {salario} e tera almento de 15% total a ser pago {total2}')
