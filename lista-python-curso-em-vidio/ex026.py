frase = str(input('Digite uma frase:   ')).upper().strip()

verificar = frase.count('A')
verificar1 = frase.find('A') + 1
verificar3 = frase.rfind('A') + 1

print(verificar)
print(verificar1)
print(verificar3)