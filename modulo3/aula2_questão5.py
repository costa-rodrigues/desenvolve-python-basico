# Solicitando os dados do usuário
genero = input("Digite seu gênero (Masculino ou Feminino): ")
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço em anos: "))

# Expressão lógica para verificar as condições de aposentadoria
pode_aposentar = (
    (genero == 'F' and idade > 60) or
    (genero == 'M' and idade > 65) or
    (tempo_servico >= 30) or
    (idade >= 60 and tempo_servico >= 25)
)

# Imprimindo o resultado
print(pode_aposentar)