# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Definindo as vogais
vogais = "aeiouAEIOU"

# Inicializa uma nova string para armazenar a frase modificada
frase_modificada = ""

# Percorre cada caractere da frase original
for caractere in frase:
    # Substitui o caractere se for uma vogal
    if caractere in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += caractere

# Exibe a frase modificada
print("Frase modificada:", frase_modificada)