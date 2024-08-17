import random

def imprime_enforcado(erros):
    """Imprime o estágio do enforcado de acordo com o número de erros."""
    with open('gabarito_enforcado.txt', 'r') as arquivo:
        enforcados = arquivo.readlines()
        print(enforcados[erros].strip())

def jogar_forca():
    """Função principal do jogo da forca."""
    with open('gabarito_forca.txt', 'r') as arquivo:
        palavras = arquivo.read().splitlines()

    palavra_secreta = random.choice(palavras)
    letras_acertadas = ['_' for letra in palavra_secreta]
    erros = 0

    print("Bem-vindo ao jogo da forca!")
    print(''.join(letras_acertadas))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in palavra_secreta:
            for i, letra_palavra in enumerate(palavra_secreta):
                if letra == letra_palavra:
                    letras_acertadas[i] = letra
        else:
            erros += 1
            imprime_enforcado(erros)

        print(''.join(letras_acertadas))

        if '_' not in letras_acertadas:
            print("Parabéns, você venceu!")
            break
        elif erros == 6:
            print("Você perdeu! A palavra era:", palavra_secreta)
            break

if __name__ == "__main__":
    jogar_forca()