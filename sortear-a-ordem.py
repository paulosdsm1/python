import random

# Solicita ao usuário para inserir os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Coloca os nomes dos alunos em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralha a lista de alunos
random.shuffle(alunos)

# Mostra a ordem sorteada na tela
print("A ordem de apresentação será: {', '.join(alunos)}")
