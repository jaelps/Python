totalmaior = 0
totalmenor = 0
for pessoa in range(1,8):
    idade = int(input(f'Em que ano a {pessoa}ª você nasceu?  '))
    ano = 2022 - idade
    if ano >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print(f'no total tivemos {totalmaior} pessoas maior de idade')
print(f'e tivemos {totalmenor} menor de idade')