# Lê a temperatura em graus Fahrenheit 
fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))

# Converte a temperatura de Fahrenheit para Celsius 
celsius = (fahrenheit - 32) * (5 / 9)

# Imprime o resultado com a formatação especificada
print(f"{fahrenheit} graus Fahrenheit são {int(celsius)} graus Celsius.")