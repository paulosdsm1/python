reais = float(input('Quanto dinheiro você tem: '))
dolar = reais / 5.05
euro = reais / 5.36

print('Com {:.2f} reias você consegue comprar {:.2f} dolar ou {:.2f} euros' .format(reais, dolar, euro))