argumentos e parametros
argumentos sao enviados para funcao ao ser chamada

os parametros sao os argumentos recebidos pela funcao e ela vai tratar esses dados para retornar algo

def get_msg(n):
    x = n + 1

    return x
messagem = get_msg(1)
print(messagem)

o numero de argumentos devem ter o mesmo numero de parametros esperados pela funcao

parametro padrao
valor padrao

argumento nomeado
com argumentos nomeados nao importa a ordem de envio dos argumentos

def my_funcition(name = "pitu", animal = "cachorro")

def my function(frutas):
    for fruta in frutas
    print(fruta)

frutas =["maca", "banana", "uva", "laranja"]
print(type(frutas))
my_funciton(frutas)

def my_function(*numbers)
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))