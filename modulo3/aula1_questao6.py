#iniciar as variaveis , resultado e controle
n = int(input("quantidade de cobaias: 2"))
cont = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

#interações
while cont < n:
    quantia = int(input())
    tipo = input()

    if tipo == 'S':
        soma_sapo += quantia
    elif tipo == 'R':
        soma_rato += quantia
    elif tipo =='C':
        soma_coelho += quantia
               


    cont += 1

print("total de cobaias: ", soma_sapo+soma_rato+soma_coelho)
print("total de sapos: ", soma_sapo)   
print("total de ratos: ", soma_rato)  
print("total de coelhos: ", soma_coelho)   