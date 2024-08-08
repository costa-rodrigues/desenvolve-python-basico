# Solicitar a entrada do número de respondentes
n = int(input("Digite a quantidade de respondentes: "))

# Inicializar as variáveis
soma = 0  # resultado --> soma
cont = 0  # variável de controle do laço

# Ler as N idades
while cont < n:
    idade = int(input(f"Digite a idade do respondente {cont + 1}: "))
    soma += idade  # soma = (soma + idade)
    cont += 1  # cont = cont + 1

# Calcular e imprimir a média
media = soma / n
print(f"A idade média é {media:.0f} anos")