print("Bem vindo ao app Y")
print("1: cadastro")
print("2: login")
print("3: sair")
menu = int(input("escolha uma das opções acima:"))
match menu:
    case 1:
        print("cadastro")
    case 2:
        print("login")
    case 3:
        print("sair")
    case _:
        print("opção invalida")