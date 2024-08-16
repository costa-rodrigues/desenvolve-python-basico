# Lista dos meses do ano por extenso
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Solicita a data de nascimento no formato dd/mm/aaaa
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Divide a data em dia, mês e ano
dia, mes, ano = data_nascimento.split('/')

# Converte o mês para o nome do mês por extenso (subtrai 1 para ajustar o índice da lista)
mes_extenso = meses[int(mes) - 1]

# Exibe a data formatada
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")