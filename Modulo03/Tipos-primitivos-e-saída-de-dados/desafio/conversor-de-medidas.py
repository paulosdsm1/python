medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000

print('{:.0f} em cm é igual a {:.0f} e em km é {:.0f}' .format(medida, cm, mm))