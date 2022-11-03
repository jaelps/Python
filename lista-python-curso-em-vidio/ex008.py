medida = float(input('Digite a medida a ser verificada:   '))

km = medida / 1000
hm = medida /100
dam = medida / 10
dm = medida * 10
cent = medida *100
mili = medida *1000

print(f'O valor me metros {medida}m')
print(f' kilometo: {km}\n horametro: {hm}\n diametro: {dam}\n decimetro: {dm}\n centimtro: {cent}\n milimetro: {mili}')
