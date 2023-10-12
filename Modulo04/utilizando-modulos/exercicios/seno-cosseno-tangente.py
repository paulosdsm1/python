import math

# Solicita ao usuário para inserir o ângulo
angulo = float(input("Digite o valor do ângulo: "))

# Converte o ângulo de graus para radianos
angulo_rad = math.radians(angulo)

# Calcula o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Mostra os resultados na tela
print("O seno do ângulo {angulo} é {seno:.2f}")
print("O cosseno do ângulo {angulo} é {cosseno:.2f}")
print("A tangente do ângulo {angulo} é {tangente:.2f}")
