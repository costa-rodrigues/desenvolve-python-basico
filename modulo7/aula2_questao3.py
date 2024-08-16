import string

def e_palindromo(frase):
    # Remove espaços, pontuação e converte para minúsculas
    frase_limpa = ''.join(char.lower() for char in frase if char.isalnum())
    # Verifica se a frase limpa é igual ao seu reverso
    return frase_limpa == frase_limpa[::-1]

while True:
    # Solicita uma frase ao usuário
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    # Verifica se o usuário quer encerrar o programa
    if frase.lower() == "fim":
        break
    
    # Verifica se a frase é um palíndromo e exibe o resultado
    if e_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')