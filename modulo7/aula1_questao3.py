
def contar_espacos(frase):
  """Conta o número de espaços em branco em uma frase.

  Args:
    frase: A frase a ser analisada.

  Returns:
    int: O número de espaços em branco na frase.
  """

  # Conta o número de ocorrências do espaço em branco na frase
  num_espacos = frase.count(" ")
  return num_espacos

# Solicita a frase ao usuário
frase = input("Digite a frase: ")

# Chama a função para contar os espaços e exibe o resultado
resultado = contar_espacos(frase)
print(f"Espaços em branco: {resultado}")