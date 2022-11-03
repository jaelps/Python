import math

angulo = float(input('digite o anjulo: '))

c = math.cos((math.radians(angulo)))
s = math.sin((math.radians(angulo)))
t = math.tan((math.radians(angulo)))

print(f'Angulo em graus informado  {angulo:.2f}\n coseno  {c:.2f}\nseno  {s:.2f}\ntangente  {t:.2f}')