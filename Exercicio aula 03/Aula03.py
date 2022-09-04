valor1 = int(input("Digite o munero 1: "))
valor2 = int(input("Digite o munero 2: "))

resto1 = valor1%2
resto2 = valor2%2

if resto1 == 0: 
    print("O primeiro número digitado é par.")
else:
    print("O primeiro número digitado é impar.")

if resto2 == 0:
     print("O segundo número digitado é par.")
else:
    print("O segundo número digitado é impar.")

if valor1 <10:
    print ("O primeiro número é menor que 10.")
elif valor1>10:
    print("O primeiro número é maior que 10.")

if valor2 <10:
    print ("O segundo número é menor que 10.")
elif valor2>10:
    print("O segundo número é menor que 10.")

print(f"O quadrado do primeiro número é: {valor1**2:.2f}")
print(f"O quadrado do segundo número é: {valor2**2:.2f}")

print(f"O resto da divisão do primeiro numero por 2 é: {resto1}")
print(f"O resto da divisão do segundo numero por 2 é: {resto2}")

print(f"A soma dos 2 numeros é: {valor1+valor2}")