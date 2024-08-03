#exercício 1

# Lê o comprimento do terreno como um número inteiro
comprimento = int(input("comprimento do terreno (em metros): "))

# Lê a largura do terreno como um número inteiro
largura = int(input("largura do terreno (em metros): "))

# Lê o preço do metro quadrado como um número de ponto flutuante
preco_metro_quadrado = float(input("Digite o preço do metro quadrado (em reais): "))

# Calcula a área do terreno
area = comprimento * largura

# Calcula o preço total do terreno
preco_terreno = area * preco_metro_quadrado

# Imprime o resultado 
print(f"O terreno possui {area}m2 e custa R${preco_terreno:,.2f}")

