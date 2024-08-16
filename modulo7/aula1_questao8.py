def validar_cpf(cpf):
    """Valida um CPF fornecido no formato XXX.XXX.XXX-XX.

    Args:
        cpf (str): O CPF a ser validado.

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """

    # Remove caracteres não numéricos
    cpf = cpf.replace('.', '').replace('-', '')

    # Verifica se o CPF tem 11 dígitos e não é uma sequência repetitiva
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Verifica se os dígitos verificadores calculados são iguais aos dígitos informados
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

# Solicita o CPF ao usuário
cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

# Valida o CPF e imprime o resultado
if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")