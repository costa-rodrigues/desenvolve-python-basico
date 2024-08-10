import datetime

# Obtém a data e hora atuais
agora = datetime.datetime.now()

# Formata a data e a hora
data_formatada = f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}"
hora_formatada = f"Hora: {agora.hour:02d}:{agora.minute:02d}"

# Imprime a data e a hora formatadas
print(data_formatada)
print(hora_formatada)