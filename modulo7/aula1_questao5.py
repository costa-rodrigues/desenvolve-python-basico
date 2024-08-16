def contar_vogais(frase):
    """Conta o número de vogais em uma frase e retorna seus índices.

    Args:
        frase: A frase a ser analisada.

    Returns:
        tuple: Uma tupla contendo o número de vogais e uma lista com os índices.
    """

    vogais = "aeiouAEIOU"
    indices_vogais = []

    for i, letra in enumerate(frase):
        if letra in vogais:
            indices_vogais.append(i)

    return len(indices_vogais), indices_vogais

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Chama a função para contar as vogais e obter os índices
num_vogais, indices = contar_vogais(frase)

# Imprime o resultado
print(f"{num_vogais} vogais")
print(f"Índices: {indices}")