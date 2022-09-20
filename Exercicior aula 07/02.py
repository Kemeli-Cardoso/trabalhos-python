pessoas=int(input("Digite o numero de pessoas em sua familia: "))
Salario1=float(input("Digite o salario 1: "))
Salario2=float(input("Digite o salario 2: "))
Salario3=float(input("Digite o salario 3: "))
Salario4=float(input("Digite o salario 4: "))
salariototal=Salario1+Salario2+Salario3+Salario4
media=salariototal/pessoas
if media>=3801.00:
    print(f"O valor medio salarial é de {media}, e sua classe é ALTA")
elif media>=2750.01 and media<=3800.99:
    print(f"O valor medio salarial é de {media}, e sua classe é MEDIA ")
elif media>=2750.00:
    print(f"O valor medio salarial é de {media}, e sua classe é BAIXA")