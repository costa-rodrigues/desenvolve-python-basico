def nome_em_escada(nome):
  """Imprime o nome em formato de escada.

  Args:
    nome: O nome a ser impresso.
  """

  for i in range(1, len(nome) + 1):
    print(nome[:i])

# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Chama a função para imprimir o nome em formato de escada
nome_em_escada(nome)