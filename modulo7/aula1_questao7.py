import random

def encrypt(nomes):
    """Criptografa uma lista de nomes, substituindo cada caracter por seu equivalente + n, onde n é um número aleatório entre 1 e 10.

    Args:
        nomes (list): Lista de nomes a serem criptografados.

    Returns:
        tuple: Uma tupla contendo a lista de nomes criptografados e a chave utilizada.
    """

    # Gera a chave aleatória
    chave = random.randint(1, 10)

    # Criptografa cada nome
    nomes_criptografados = []
    for nome in nomes:
        nome_criptografado = ""
        for letra in nome:
            # Converte a letra para um número inteiro, adiciona a chave e converte de volta para caractere
            novo_caractere = chr(ord(letra) + chave)
            # Garante que o caractere permaneça no intervalo visível
            while ord(novo_caractere) > 126:
                novo_caractere = chr(ord(novo_caractere) - 94)  # Volta para o início do intervalo visível
            nome_criptografado += novo_caractere
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave

# Exemplo de uso
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print("Nomes criptografados:", nomes_criptografados)
print("Chave:", chave)