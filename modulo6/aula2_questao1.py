import random


aleatorios = []
for i in range(20):
  valor = random.randint(-100, 100)
  aleatorios.append(valor)

  print(sorted(aleatorios))
  print(aleatorios)
  print("o maior valor está no índice: ", 
        aleatorios.index(max(aleatorios)) )
  
  print("o menor valor está no índice: ", 
        aleatorios.index(min(aleatorios)))