# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais na frase, ordenadas alfabeticamente
vogais = sorted([char for char in frase if char.lower() in 'aeiou'])
print("Vogais:", vogais)

# Lista de consoantes na frase
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']
print("Consoantes:", consoantes)