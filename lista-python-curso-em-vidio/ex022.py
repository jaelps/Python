nome = input('Digite seu nome completo:  ').strip()

print(f'O seu nome em menusculo:  {nome.lower()}')
print(f'O seu nome em maiusculo: {nome.upper()}')
print(f'Qntas letras tem a string: {len(nome)}')
#print(''(.len(nome) - nome.count(' '))


dividido = nome.split()

print(f'O seu primeiro nome tem:  {len(dividido[0])} caracteris')

reconst = ''.join(dividido)
print(f'Sem o espaço o seu nome tem:  {len(reconst)} caracteris')