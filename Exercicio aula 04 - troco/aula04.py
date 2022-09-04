valor= int(input("Digite o valor: "))

notas100 = int(valor/100)
resto100 = valor%100

notas50 = int(resto100/50)
resto50 = resto100%50

notas20 = int(resto50/20)
resto20 = resto50%20

notas10 = int(resto20/10)
resto10 = resto20%10

notas5 = int(resto10/5)
resto5 = resto10%5

notas2 = int(resto5/2)
resto2 = resto5%2

moeda = int(resto2/1)

print(f"Para o valor de R${valor} será necessário: ")
if notas100 > 0:
    print(f"{notas100} notas de R$100,00")
if notas50 > 0:
    print(f"{notas50} notas de R$50,00")
if notas20 > 0:
    print(f"{notas20} notas de R$20,00")
if notas10 > 0:
    print(f"{notas10} notas de R$10,00")
if notas5 > 0:
    print(f"{notas5} notas de R$5,00")
if notas2 > 0:
    print(f"{notas2} notas de R$2,00")
if moeda > 0:
    print(f"{moeda} moedas de R$1,00")
