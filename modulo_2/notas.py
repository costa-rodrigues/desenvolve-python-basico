#leitura de dados (entrada)
valor = int(input("digite o valor: "))

#processamento
####quantidade da maior nota
nota_100 = valor // 100 #(576/100 sem o resto)
# resto da divisão
valor = valor % 100 #(576/100= 5 e restam 76)

nota_50 = valor // 50 #resto(70/50= 1 sem o resto)
valor = valor % 50 #(70/50= 1 e restam 26)

nota_20 = valor // 20 #resto(26/20 = 1 sem o resto)
valor = valor % 20 #(26/20= 1 e restam 06)

nota_10 = valor // 10 #resto(6/10 = 0 )
valor = valor % 10 #(6/10= 0)

nota_5 = valor // 5 #resto(6/5 = 1 sem o resto)
valor = valor % 5 #(6/5= 1 e restam 01)

nota_2 = valor // 2 #resto(1/2 = 0 )
valor = valor % 2 #(1/2= 0)

nota_1 = valor 

#quantidade de notas
print(f"{nota_100} notas de 100")
print(f"{nota_50} notas de 50")
print(f"{nota_20} notas de 20")
print(f"{nota_10} notas de 10")
print(f"{nota_5} notas de 5")
print(f"{nota_2} notas de 2")
print(f"{nota_1} notas de 1")