def salvar_frase():
  """Solicita uma frase ao usuário e salva em um arquivo 'frase.txt'.

  Imprime o caminho completo do arquivo salvo.
  """

  frase = input("Digite uma frase: ")

  # Abre o arquivo em modo de escrita ('w')
  with open('frase.txt', 'w') as arquivo:
    arquivo.write(frase)

  # Imprime o caminho completo do arquivo
  import os
  caminho_atual = os.getcwd()
  caminho_completo = os.path.join(caminho_atual, 'frase.txt')
  print(f"Frase salva em {caminho_completo}")

if __name__ == "__main__":
  salvar_frase()