numero = input('Digite um numero:  ')

print(f'O numero infomrado foi:  {numero}')

dividido = numero.split()
#dividido = numero

print(f'Unidade: {dividido[3]}')
print(f'Dezena:  {dividido[2]}')
print(f'Centena: {dividido[1]}')
print(f'Milhar:  {dividido[0]}')

#------------------------------------------utilizado int
numero = int(input('digite um numero:  '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena:  {d}')
print(f'Centena: {c}')
print(f'Milhar:  {m}')

