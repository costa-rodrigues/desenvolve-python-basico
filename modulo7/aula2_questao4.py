import re

def validador_senha(senha):
    # Verifica o comprimento mínimo
    if len(senha) < 8:
        return False
    
    # Verifica se contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False
    
    # Verifica se contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False
    
    # Verifica se contém pelo menos um número
    if not re.search(r'\d', senha):
        return False
    
    # Verifica se contém pelo menos um caractere especial
    if not re.search(r'[@#$%^&*(),.?!{}|<>]', senha):
        return False
    
    # Se todas as verificações passaram
    return True

# Exemplo de uso da função
senha = input("Digite uma senha para verificar: ")
if validador_senha(senha):
    print("Senha válida.")
else:
    print("Senha inválida. Certifique-se de que a senha atende a todos os critérios.")