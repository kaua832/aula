idade = int(input("digite a idade "))
if idade <= 12:
    print("crianca")
elif idade < 18:
    print("adolescente")
elif idade < 65:
    print("adulto")
else:
    print("idoso")