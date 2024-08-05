# Solicita os dois números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Verifica se a soma é par ou ímpar
if soma % 2 == 0:
    print(f"A soma de {numero1} e {numero2} é {soma}, que é um número par.")
else:
    print(f"A soma de {numero1} e {numero2} é {soma}, que é um número ímpar.")