import math

catetoOposto = float(input('Digite: '))
catetoAdjasente = float(input('Digite: '))

ipotenusa = (catetoOposto**2 + catetoAdjasente**2) **(1/2)
ipotenusa2 = math.hypot(catetoAdjasente, catetoOposto)

print(f'o valor da ipotenusa é {ipotenusa:.2f}')