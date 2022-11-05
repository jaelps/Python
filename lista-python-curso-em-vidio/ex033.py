a = int(input('Primeiro numero:  '))
b = int(input('Segundo numero:   '))
c = int(input('Terceiro numero:  '))

#vrificado que é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#verificado que é o maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior é {maior}')
print(f'O menor é {menor}')