a = [1, 2]
b = [1, 2]
c = a
a==b # True os valores sao iguais
a is b  # False sao listas diferentes em lugares diferentes da memoria(nao e a mesma coisa, nao sao os mesmos elementos)
a is c # True (c aponta exatamente para a mesma lista que a)
 a = [1, 2]
 b = [1, 2]
 c = a
 print (a == b)
True
 print (a is b)
False
print (a is c)
True
== (comparaçao)
is (nao e o mesmo elemento)
#Identacao

padrao oficial sao 4 espaços
pode-se usar o tab
nao se mistura tab com espaço ao identar
comentario e #
variaveis, explicitando
x = str(3) # x vai ser uma string
y = int(3) # y vai ser um inteiro
z = float(3) # z vai ser um float
b = bool(1) # b vai ser um booleano

saber o tipo de variavel
print(type(x))

Atribuicao de multiplas variaveis
x, y, z = "laranja", "morango", "banana"

condicional simples: if
temperatura 30
if temperatura > 25:
    print("esta calor")
    else: