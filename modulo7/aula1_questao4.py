def formatar_telefone(numero):
    """Formata um número de telefone brasileiro com 9 dígitos e adiciona um hífen.

    Args:
        numero: O número de telefone a ser formatado.

    Returns:
        str: O número de telefone formatado.
    """

    numero = str(numero)  # Garante que o número seja uma string

    if len(numero) == 8:
        # Adiciona o dígito 9 no início
        numero = "9" + numero
    elif len(numero) == 9 and numero[0] != '9':
        print("O primeiro dígito deve ser 9 para números brasileiros.")
        return None
    
    # Formata o número com o hífen
    return f"{numero[:5]}-{numero[5:]}"

# Solicita o número de telefone ao usuário
numero = input("Digite o número: ")

# Chama a função para formatar o número e exibe o resultado
numero_formatado = formatar_telefone(numero)
if numero_formatado:
    print(f"Número completo: {numero_formatado}")