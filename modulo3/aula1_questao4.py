def encontrar_maior_numero(n):
    """Encontra o maior número em uma sequência de n números.

    Args:
        n: O número de elementos da sequência.

    Returns:
        O maior número da sequência.
    """

    maior = 0
    for _ in range(n):
        x = int(input("Digite um número: "))
        maior = max(maior, x)
    return maior

# Exemplo de uso:
n = int(input("Digite a quantidade de números: "))
resultado = encontrar_maior_numero(n)
print("O maior número é:", resultado)