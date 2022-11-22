n = int(input('Digite um umero interio:    '))
conv = str(input('Se você deseja coverter digite uma opção binario(1) / octal(2) / hexadecimal(3)'))

1
2
3

if conv == 1:
    print('O numero {n} convertido em binario ficaria {}')
elif conv == 2:
    print('O numero {n} comvertido em octal ficaria {}')
else:
    print('O numero {n} convertido em hexadecimal ficaria {}')