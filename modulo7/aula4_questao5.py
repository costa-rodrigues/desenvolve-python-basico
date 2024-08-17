import csv

# Lista de livros (substitua pelos seus dados)
livros = [
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["1984", "George Orwell", 1949, 328],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 279],
    # Adicione mais livros aqui
]

# Cabeçalho da tabela
cabecalho = ["Título", "Autor", "Ano de publicação", "Número de páginas"]

# Abre o arquivo CSV para escrita
with open('meus_livros.csv', 'w', newline='') as csvfile:
    # Cria um objeto escritor
    escritor = csv.writer(csvfile)

    # Escreve o cabeçalho
    escritor.writerow(cabecalho)

    # Escreve as informações dos livros
    escritor.writerows(livros)

print("Arquivo 'meus_livros.csv' criado com sucesso!")