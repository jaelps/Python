
valor = float(input('Valor do produto:  '))

avista = ((valor * 0.10) - valor)* - 1
cart = ((valor * 0.05) - valor)* - 1
parc2 = valor /2
parc3 =(valor * 0.20) + valor
parc0 = parc3 / 3

pag = float(input('''Forma de pagamento
 [ 1 ] à vista ou cheque : 10% desconto
 [ 2 ] cartão de credito : 5% desconto
 [ 3 ] parcelado 2x cartão
 [ 4 ] parcelado 3x ou mais cartão: puros 20% \n'''))

print(f'Valor do produto {valor}')

if pag == 1:
    print(f'Com o desconto 10% para pagamento à vista {avista}')
elif pag == 2:
    print(f'Com o desconto de 5% para pagamento à vista em cartão {cart}')
elif pag == 3:
    print(f'''Não possui desconto para pagamento parcelado:
    em 2x valor {parc2}''')
else:
    print(f'''Parcelametos a cima de 3x tem 20% juros o valor para pagamento {parc3} parcelado:
    3x {parc0}
    4x {parc3 / 4}
    5x {parc3 / 5}''')


