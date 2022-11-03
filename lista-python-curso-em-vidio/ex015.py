dist = float(input('Digite a distancia percorrida em Km: '))
dias = int(input('Digite a quantidade de dias o carro foi utilizado: '))
Cdia = 60
disK = 0.15
#sugestão ---> pago = (dias * 60) + (km * 0.15)

totalP = dist * disK
totalD = dias * Cdia

total = totalD + totalP

print(f'Total do carro por dias {totalD} e total por litros de gasolina utilizado R${totalP}\n Total a pagar {total}')