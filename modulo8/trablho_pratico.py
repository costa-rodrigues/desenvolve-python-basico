import csv

# Função para carregar usuários de um arquivo CSV
def carregar_usuarios():
    usuarios = {}
    with open('usuarios.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios[int(row['id'])] = {
                'nome': row['nome'],
                'tipo': row['tipo'],
                'login': row['login'],
                'senha': row['senha']
            }
    return usuarios

# Função para salvar usuários em um arquivo CSV
def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'nome', 'tipo', 'login', 'senha'])
        for id, dados in usuarios.items():
            writer.writerow([id, dados['nome'], dados['tipo'], dados['login'], dados['senha']])

# Função para adicionar um novo usuário (Create)
def adicionar_usuario(usuarios):
    novo_id = max(usuarios.keys()) + 1 if usuarios else 1
    nome = input('Nome do usuário: ')
    tipo = input('Tipo de usuário (gerente, funcionário, cliente): ')
    login = input('Login: ')
    senha = input('Senha: ')
    usuarios[novo_id] = {'nome': nome, 'tipo': tipo, 'login': login, 'senha': senha}
    salvar_usuarios(usuarios)
    print(f'Usuário {nome} adicionado com sucesso!')

# Função para listar todos os usuários (Read)
def listar_usuarios(usuarios):
    for id, dados in usuarios.items():
        print(f"ID: {id}, Nome: {dados['nome']}, Tipo: {dados['tipo']}")

# Função para atualizar as informações de um usuário (Update)
def atualizar_usuario(usuarios):
    id = int(input('ID do usuário a ser atualizado: '))
    if id in usuarios:
        nome = input(f"Novo nome (atual: {usuarios[id]['nome']}): ")
        tipo = input(f"Novo tipo (atual: {usuarios[id]['tipo']}): ")
        login = input(f"Novo login (atual: {usuarios[id]['login']}): ")
        senha = input(f"Nova senha: ")
        usuarios[id] = {'nome': nome, 'tipo': tipo, 'login': login, 'senha': senha}
        salvar_usuarios(usuarios)
        print('Usuário atualizado com sucesso!')
    else:
        print('Usuário não encontrado!')

# Função para remover um usuário (Delete)
def remover_usuario(usuarios):
    id = int(input('ID do usuário a ser removido: '))
    if id in usuarios:
        del usuarios[id]
        salvar_usuarios(usuarios)
        print('Usuário removido com sucesso!')
    else:
        print('Usuário não encontrado!')

# Função de login (Controle de Acesso)
def login(usuarios):
    login = input('Login: ')
    senha = input('Senha: ')
    for id, dados in usuarios.items():
        if dados['login'] == login and dados['senha'] == senha:
            print(f"Bem-vindo {dados['nome']}!")
            return dados['tipo']
    print('Login ou senha inválidos.')
    return None

# Função principal
def main():
    usuarios = carregar_usuarios()
    tipo_usuario = login(usuarios)

    if tipo_usuario == 'gerente':
        while True:
            print('1. Adicionar usuário')
            print('2. Listar usuários')
            print('3. Atualizar usuário')
            print('4. Remover usuário')
            print('5. Sair')
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                adicionar_usuario(usuarios)
            elif opcao == 2:
                listar_usuarios(usuarios)
            elif opcao == 3:
                atualizar_usuario(usuarios)
            elif opcao == 4:
                remover_usuario(usuarios)
            elif opcao == 5:
                break
            else:
                print('Opção inválida!')

    elif tipo_usuario == 'funcionario':
        # Funcionalidades específicas para funcionário (ex: gerenciar produtos)
        pass

    elif tipo_usuario == 'cliente':
        # Funcionalidades específicas para cliente (ex: visualizar produtos)
        pass

    else:
        print('Acesso negado!')

if __name__ == '__main__':
    main()

    