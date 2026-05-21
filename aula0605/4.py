status_code = 404
match status_code:
    case 200:
        print("sucesso")
    case 404:
        print("nao encontrado")
    case 500:
        print("erro no servidor")
    case _:
        print("codigo desconhecido")