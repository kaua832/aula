usuarios = []
login_sucesso = False
def login():
    cpf = input("usuario: ")
    senha = input("senha: ")
    global login_sucesso
    login_sucesso = False
    for u in usuarios:
        if u["usuario"] == nome and u["senha"] == senha:
            login_sucesso = True
            break
    print("acesso liberado" if login_sucesso else "falha no login")

def trocar_senha():
    nome = input("usuario: ")
    senha_atual = input("senha atual: ")
    for user in usuarios:
        if user["usuario"] == nome and user["senha"] == senha_atual:
            user["senha"] = input("Nova senha: ")
            print("senha atualizada")
            return
    print("dados invalidos")
    
def cadastrar():
    nome = input("novo usuario: ")
    senha = input("senha: ")
    cpf = int(input("CPF(apenas os numeros)"))
    usuarios.append({"usuario": nome, "senha": senha, "cpf": cpf})
    print(f"usuario {nome} cadastrado com sucesso")

def sistema():
    while True:
        global login_sucesso
        if login_sucesso:
            print("\n1. login | 2. trocar senha| 3. sair")
            opcao = input("escolha: ")

            match opcao:
                case "1":
                    login()
                case "2":
                    trocar_senha()
                case "3":
                    print("saindo...")
                    login_sucesso = False
                    
                case _:
                    print("opcao invalida")
        else:
            print("\n1. cadastrar | 2. login | 3. trocar senha | 4. sair do programa")
            opcao = input("escolha: ")

            match opcao:
                case "1":
                    cadastrar()
                case "2":
                    login()
                case "3":
                    trocar_senha()
                case "4":
                    print("saindo...")
                    
                    
                    break
                case _:
                    print("opcao invalida")

sistema()