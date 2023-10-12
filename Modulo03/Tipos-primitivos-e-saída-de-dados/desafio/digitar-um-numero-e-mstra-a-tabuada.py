# Solicita ao usuário que insira um número
num = int(input("Digite um número para ver sua tabuada: "))

# Loop para calcular e imprimir a tabuada
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")