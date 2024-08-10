import emoji

# Dicionário com emojis e seus códigos
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "": ":thumbs_up:",
    "": ":thinking_face:",
    "": ":partying_face:"
}

# Apresenta a lista de emojis disponíveis
print("Emojis disponíveis:")
for emoji, codigo in emojis_disponiveis.items():
    print(f"{emoji} - {codigo}")

# Solicita a frase ao usuário
frase = input("Digite uma frase e ela será emojizada: ")

# Função para emojizar a frase
def emojizar(frase):
    for emoji, codigo in emojis_disponiveis.items():
        frase = frase.replace(codigo, emoji)
    return frase

# Emojiza a frase e imprime o resultado
frase_emojizada = emojizar(frase)
print("Frase emojizada:")
print(frase_emojizada)