numero = int(input('Digite um numero:  '))

print('''Escolha uma das bases para coversão:
[ 1 ] converte para Binario
[ 2 ] converte para Octal
[ 3 ] converte para Hexadecimal''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{numero} convertido para binario é {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para octal é {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido em hexadecimal é {hex(numero)[2:]}')
else:
    print('Digite uma opção valida!!')


