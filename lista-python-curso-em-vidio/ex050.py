cont = 0
soma = 0
for i in range(1,7):
    num = int(input('Digite o numero:  '))
    if num % 2 == 0:
        soma = num + soma
        cont = cont + 1
print(f'Você informou {cont} numeros pares a soma total é {soma}')