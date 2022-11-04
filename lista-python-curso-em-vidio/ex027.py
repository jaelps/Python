nome = input('digite seu nome completo:   ').strip()

s = nome.split()

print(f'O primeiro nome é {s[0]}')
print(f'O seu umtimo nome é {s[2]}')
print(f'{s[len(s) -1]}')