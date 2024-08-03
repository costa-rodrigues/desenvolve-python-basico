#leitura de dados (entrada)
nome_produto1 = input("Digite o nome do produto 1:")
valor_produto1 = float(input("Digite o valor do produto 1: "))
quantidade_produto1 = int(input("quantidade do produto 1: "))

nome_produto2 = input("Digite o nome do produto 2:")
valor_produto2 = float(input("Digite o valor do produto 2: "))
quantidade_produto2 = int(input("quantidade do produto 2: "))

nome_produto3 = input("Digite o nome do produto 3:")
valor_produto3 = float(input("Digite o valor do produto 3: "))
quantidade_produto3 = int(input("quantidade do produto 3: "))

#processamento
####multiplicando o valor pela quantidade
total_produto1 = float(valor_produto1 * quantidade_produto1)

total_produto2 = float(valor_produto2 * quantidade_produto2)

total_produto3 = float(valor_produto3 * quantidade_produto3)

#calculando o valor gasto com cada produto
print(f"foi comprado(a){quantidade_produto1}  {nome_produto1} , custando cada unidade {valor_produto1} , o preço total gasto com este produto é R${total_produto1:,.2f}")
print(f"foi comprado(a){quantidade_produto2}  {nome_produto2} , custando cada unidade {valor_produto2} , o preço total gasto com este produto é R${total_produto2:,.2f}")
print(f"foi comprado(a){quantidade_produto3}  {nome_produto3} , custando cada unidade {valor_produto3} , o preço total gasto com este produto é R${total_produto3:,.2f}")

#calculando o valor gasto com todos os produtos
total_gasto = (total_produto1 + total_produto2 + total_produto3)

#valor total gasto na compra
print(f"O valor total gasto com a compra dos produtos é : R$ {total_gasto:,.2f}")