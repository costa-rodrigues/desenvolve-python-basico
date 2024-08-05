# Solicita a distância da entrega em quilômetros
distancia = float(input("Digite a distância da entrega em quilômetros: "))

# Solicita o peso do pacote em quilogramas
peso = float(input("Digite o peso do pacote: "))

# Calcula o valor do frete com base na distância
if  distancia <= 100:
    valor_frete = peso * 1.0
elif 101 <= distancia <= 300:
    valor_frete = peso * 1.5
else:
    valor_frete = peso * 2.0

# Acrescenta uma taxa de R$10 para pacotes com peso superior a 10 kg
if peso > 10:
    valor_frete += 10.0

# Imprime o valor do frete
print(f"O valor do frete é: R${valor_frete:.2f}")