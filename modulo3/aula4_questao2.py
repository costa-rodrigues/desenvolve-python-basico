# Solicita ao usuário a nota referente ao filme
nota_filme = int(input("Digite a nota de 1 até 5 referente ao que vocé achou do filme: "))

# Verifica em qual modalidade a nota está
if nota_filme == 5:
    print(f" Excelente!")
elif nota_filme == 4:
    print(f"Muito Bom !")
elif nota_filme == 3:
    print(f" Bom !")
elif nota_filme == 2:
    print(f" Regular !")
elif nota_filme == 4:
    print(f" Ruim !")
else:
    print("Avaliação inválida. Por favor, insira um número de 1 a 5.")


    