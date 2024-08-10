import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

while True:
    chute = int(input("Adivinhe o número entre 1 e 10: "))

    if chute < numero_secreto:
        print("Muito baixo, tente novamente!")
    elif chute > numero_secreto:
        print("Muito alto, tente novamente!")
    else:
        print("Correto! O número é", numero_secreto)
        break