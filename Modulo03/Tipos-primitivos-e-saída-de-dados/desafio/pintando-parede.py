# Solicita ao usuário a largura e a altura da parede
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área da parede
area = largura * altura

# Calcula a quantidade de tinta necessária (cada litro pinta 2 metros quadrados)
litros_tinta = area / 2

print("A área da parede é de {:.2f} metros quadrados." .format(area))
print("Você precisará de {:.2f} litros de tinta para pintar a parede." .format(litros_tinta))
