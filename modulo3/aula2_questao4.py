# Solicita a classe do personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()

# Solicita os pontos de força e magia do personagem
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Dicionário com as condições de validação para cada classe
requisitos = {
    "guerreiro": lambda forca, magia: forca >= 15 and magia <= 10,
    "mago": lambda forca, magia: forca <= 10 and magia >= 15,
    "arqueiro": lambda forca, magia: 5 < forca <= 15 and 5 < magia <= 15
}

# Verifica se a classe escolhida é válida e realiza a validação dos atributos
validacao = requisitos.get(classe, lambda forca, magia: False)(forca, magia)

# Imprime o resultado da validação
print("Pontos de atributo consistentes com a classe escolhida:", validacao)