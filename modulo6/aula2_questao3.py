import random
from collections import Counter

# Preencher as listas com valores aleatórios
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Criar a lista de interseccao sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

# Contagem de ocorrências em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Imprimir as listas e a interseccao
print(f'lista1 - {lista1}')
print(f'lista2 - {lista2}')
print(f'Interseccao - {interseccao}')

# Imprimir a contagem de cada elemento na interseccao
print("Contagem")
for elemento in interseccao:
    print(f'{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})')