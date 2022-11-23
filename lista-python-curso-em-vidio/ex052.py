frase = str(input('Digite uma frase:  ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(f'o inverso de {frase} é {inverso}')
if inverso == junto:
    print('Temos um palindromo!')