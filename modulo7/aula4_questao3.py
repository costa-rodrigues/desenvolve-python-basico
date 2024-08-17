def analisar_arquivo(nome_arquivo):
  """Analisa o arquivo especificado e imprime as informações solicitadas.

  Args:
    nome_arquivo: O nome do arquivo a ser analisado.
  """

  with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    # Primeiras 25 linhas
    print("Primeiras 25 linhas:")
    for i in range(25):
      print(linhas[i].strip())

    # Número total de linhas
    print(f"Número total de linhas: {len(linhas)}")

    # Linha com maior número de caracteres
    linha_maior = max(linhas, key=len)
    print(f"Linha com maior número de caracteres: {linha_maior.strip()}")

    # Contar menções a "Nonato" e "Íria"
    import re
    nonato_count = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
    iria_count = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))
    print(f"Menções a 'Nonato': {nonato_count}")
    print(f"Menções a 'Íria': {iria_count}")

# Chamar a função com o nome do arquivo
analisar_arquivo('estomago.txt')