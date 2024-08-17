import re

def separar_palavras():
  """Lê o arquivo 'frase.txt', remove espaços e caracteres não alfabéticos,
  e salva as palavras em um novo arquivo 'palavras.txt'.

  Imprime o conteúdo do arquivo 'palavras.txt'.
  """

  # Abre o arquivo 'frase.txt' para leitura
  with open('frase.txt', 'r') as arquivo:
    texto = arquivo.read()

  # Remove espaços em branco e caracteres não alfabéticos
  palavras = re.findall(r'\w+', texto)

  # Abre o arquivo 'palavras.txt' para escrita
  with open('palavras.txt', 'w') as arquivo:
    for palavra in palavras:
      arquivo.write(palavra + '\n')

  # Abre o arquivo 'palavras.txt' para leitura e imprime o conteúdo
  with open('palavras.txt', 'r') as arquivo:
    print(arquivo.read())

if __name__ == "__main__":
  separar_palavras()