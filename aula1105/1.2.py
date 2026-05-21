#funcao cadastro
def cadastro(n):
    print(f"usuaripo {n} cadastrado com sucesso!")
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


'''
print("Bem vindo ao app Y")
print("1: cadastro")
print("2: login")
print("3: sair")
'''
def menu_principal(): 
    while True:
        print("Bem vindo ao app Y")
        print("1: cadastro")
        print("2: login")
        print("3: sair\n")
        menu = int(input("escolha uma das opções acima:"))
        match menu:
            case 1:
                nome = input("qual seu nome? ")
                cadastro(nome)

            case 2:
                login()
            case 3:
                sair()
                break
            case _:
                opcaoInvalida()
menu_principal()