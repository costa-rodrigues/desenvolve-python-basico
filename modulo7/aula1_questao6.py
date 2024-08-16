from collections import Counter

def encontrar_anagramas(frase, palavra_objetivo):
    """Encontra todos os anagramas de uma palavra objetivo em uma frase.

    Args:
        frase: A frase onde procurar os anagramas.
        palavra_objetivo: A palavra para a qual se busca os anagramas.

    Returns:
        list: Uma lista com todos os anagramas encontrados.
    """

    # Cria um contador para a palavra objetivo
    contador_objetivo = Counter(palavra_objetivo)

    # Separa a frase em palavras
    palavras = frase.split()
    anagramas = []

    for palavra in palavras:
        # Cria um contador para a palavra atual
        contador_palavra = Counter(palavra)
        # Verifica se os contadores são iguais
        if contador_palavra == contador_objetivo:
            anagramas.append(palavra)

    return anagramas

# Solicita a frase e a palavra objetivo ao usuário
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

# Chama a função para encontrar os anagramas
anagramas = encontrar_anagramas(frase, palavra_objetivo)

# Imprime os anagramas
print(f"Anagramas: {anagramas}")