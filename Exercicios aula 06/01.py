altura = float(input("Digite sua altura: "))
sexo = int(input("Qual seu sexo? Digite 1 para feminino e 2 para masculino: "))
if sexo==1:
    print(f"{(62.1*altura)-44.7}")
else:
    print(f"{(72.7*altura)-58}")