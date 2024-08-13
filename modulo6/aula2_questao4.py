# Função para ler uma lista de números do usuário
def ler_lista(tamanho, numero_lista):
    lista = []
    print(f'Digite os {tamanho} elementos da lista {numero_lista}:')
    for _ in range(tamanho):
        lista.append(int(input()))
    return lista

# Ler o tamanho das listas e os elementos das listas
tamanho1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = ler_lista(tamanho1, 1)

tamanho2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = ler_lista(tamanho2, 2)

# Combinar as listas alternadamente
lista_intercalada = []
minimo_tamanho = min(tamanho1, tamanho2)

for i in range(minimo_tamanho):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adicionar os elementos remanescentes da maior lista
lista_intercalada.extend(lista1[minimo_tamanho:])
lista_intercalada.extend(lista2[minimo_tamanho:])

# Imprimir a lista intercalada
print("Lista intercalada:", " ".join(map(str, lista_intercalada)))