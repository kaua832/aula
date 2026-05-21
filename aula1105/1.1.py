#funcao cadastro
def cadastro():
    print("cadastro")
#fim do cadastro
#funcao do login
def login():
    print("login")
#fim do login
#funcao sair
def sair():
    print("sair")
#fim do sair
#funcao invalia
def opcaoInvalida():
    print("opção invalida")
#fim da funcao invalida



print("Bem vindo ao app Y")
print("1: cadastro")
print("2: login")
print("3: sair")
menu = int(input("escolha uma das opções acima:"))
match menu:
    case 1:
        cadastro()
    case 2:
        login()
    case 3:
        sair()
    case _:
        opcaoInvalida()