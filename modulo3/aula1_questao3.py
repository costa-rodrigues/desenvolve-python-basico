# Ler as três notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# Calcular a média
m = (n1 + n2 + n3) / 3

# Verificar a média e imprimir o resultado
if m >= 60:
    print("aprovado")
    print("fim")
elif m >= 40:
    print("recuperação")
    print("fim")
else:
    print("reprovado")
    print("fim")