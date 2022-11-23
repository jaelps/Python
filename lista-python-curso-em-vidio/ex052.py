num = int(input('digite um numero:  '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[mo numero {num} foi divisivel por {tot} vezes')
if tot == 2:
    print('e por isso ele é primo')
else:
    print('e por isso ele não é primo')